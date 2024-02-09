#%%
import numpy as np
import pandas as pd
from qiskit.providers import BackendV1
from qiskit.providers.models import BackendProperties

# %%
def _flatten_gate_record(data):
    flat_data = {"qubits": data["qubits"], "gate": data["gate"], "name": data["name"]}

    # Extract parameters
    parameters = data["parameters"]
    for param in parameters:
        flat_data.update(
            {
                f"{param['name']}": param["value"],
                "gate_time_unit": param["unit"],
                f"{param['name']}_date": param["date"],
            }
        )
    return pd.DataFrame([flat_data])


def _gen_gate_df(data):
    return pd.concat([_flatten_gate_record(d) for d in data])


eagle_1qbgate_set = ["id", "sx", "x"]
ECR_2qbgate_set = ["ecr"]
# def IBMQ_backendV2_to_pandas(backend:BackendV2,oneqb_gate_set:list[str]=eagle_1qbgate_set,twoqb_gate_set:list[str]=ECR_2qbgate_set):
#     gate_properties = backend.target
#     qubit_properties = gate_properties.qubit_properties
def IBMQ_properties_to_pandas(
    properties: BackendProperties,
    oneqb_gate_set: list[str] = eagle_1qbgate_set,
    twoqb_gate_set: list[str] = ECR_2qbgate_set,
):
    """
    extract an IBMQ backend properties to a pandaframes.
    Useful because calling backend.properties(datetime) allow us to fetch the properties object of the backend at the specified datetime.
    arguments:
        properties: A BackendProperties backend description object, object supplied by IBM_provider are compatible as of 9-02-2024. Mostly undocumented stuff.
                 FakeBackends in qiskit are not compatible.
        oneqb_gate_set: one qubit (non virtual) gate set to look for in the prop_dict, default to eagle's gate set.
        twoqb_gate_set: two qubit gate set to look for in the prop_dict, default to ECR based eagle's gate set
    return four objects:
        First a pandas frame of most of the interesting properties of the
            quantum computer, T1 T2 Frequencies, errors gate fidelities and time.
            More or less reproduce the IBM cloud table view of backend's properties.
        Second a pandas frame of the complete qubit properties
        Third a pandas frame of the complete gate properties
        Fourth a pandas frame of other quantities.
    Together, the second third and fourth return values contains all the available
    information in the supplied prop_dict, except maybe for the backend name.

    The last three correspond directly to three substructure in the properties dict
    that contain the actual device information. Backend name is not contained dataframe.
    """
    return IBMQ_backend_prop_dict2panda(
        properties.to_dict(), oneqb_gate_set, twoqb_gate_set
    )


def IBMQ_backend_to_pandas(
    backend: BackendV1,
    oneqb_gate_set: list[str] = eagle_1qbgate_set,
    twoqb_gate_set: list[str] = ECR_2qbgate_set,
):
    """
    extract an IBMQ backend properties to a pandaframes.
    arguments:
        backend: A Backend backend description object, object supplied by IBM_provider are compatible as of 9-02-2024. Mostly undocumented stuff.
                 FakeBackends in qiskit are not compatible.
        oneqb_gate_set: one qubit (non virtual) gate set to look for in the prop_dict, default to eagle's gate set.
        twoqb_gate_set: two qubit gate set to look for in the prop_dict, default to ECR based eagle's gate set
    return four objects:
        First a pandas frame of most of the interesting properties of the
            quantum computer, T1 T2 Frequencies, errors gate fidelities and time.
            More or less reproduce the IBM cloud table view of backend's properties.
        Second a pandas frame of the complete qubit properties
        Third a pandas frame of the complete gate properties
        Fourth a pandas frame of other quantities.
    Together, the second third and fourth return values contains all the available
    information in the supplied prop_dict, except maybe for the backend name.

    The last three correspond directly to three substructure in the properties dict
    that contain the actual device information. Backend name is not contained dataframe.
    """
    return IBMQ_backend_prop_dict2panda(
        backend.properties().to_dict(), oneqb_gate_set, twoqb_gate_set
    )


def IBMQ_backend_prop_dict2panda(
    prop_dict, oneqb_gate_set=eagle_1qbgate_set, twoqb_gate_set=ECR_2qbgate_set
):
    """
    convert an IBMQ backend property dictionnary in a pandaframes.
    arguments:
        prop_dict: property dictionnary mess from an IBMQ backend
        oneqb_gate_set: one qubit gate set to look for in the prop_dict, default to eagle's gate set.
        twoqb_gate_set: two qubit gate set to look for in the prop_dict, default to ECR based eagle's gate set
    return four objects:
        First a pandas frame of most of the interesting properties of the
            quantum computer, T1 T2 Frequencies, errors gate fidelities and time.
            More or less reproduce the IBM cloud table view of backend's properties.
        Second a pandas frame of the complete qubit properties
        Third a pandas frame of the complete gate properties
        Fourth a pandas frame of other quantities.
    Together, the second third and fourth return values contains all the available
    information in the supplied prop_dict, except maybe for the backend name.

    The last three correspond directly to three substructure in the properties dict
    that contain the actual device information. Backend name is not contained dataframe.
    """
    qubit_records = []
    qubits_dict_list = prop_dict["qubits"]
    gate_dict_list = prop_dict["gates"]
    general_dict_list = prop_dict["general"]
    gate_dataframe = _gen_gate_df(gate_dict_list)
    # print(general_dict_list)
    qubit_only_record = []
    for qubit_num, qubit_props in enumerate(qubits_dict_list):
        qubit_props_sane = {}
        qubit_only = qubit_props.copy()
        for qo in qubit_only:
            qo["qubit"] = qubit_num
            qubit_only_record.append(qo)
        for qubit_prop in qubit_props:
            qubit_props_sane[qubit_prop["name"]] = qubit_prop
        if "T2" not in qubit_props_sane:
            # print(QC_name,prop_time,qubit_props)
            qubit_props_sane["T2"] = {"unit": "us", "value": np.nan}
            # print(qubit_props_sane)
        one_qbit_filters = [
            (gate_dataframe.gate == gate_tag)
            & (gate_dataframe.qubits.apply(lambda x: qubit_num in x))
            for gate_tag in oneqb_gate_set
        ]
        two_qbit_filters = [
            (gate_dataframe.gate == gate_tag)
            & (gate_dataframe.qubits.apply(lambda x: qubit_num in x))
            for gate_tag in twoqb_gate_set
        ]
        any_1qb_filter = np.logical_or.reduce(one_qbit_filters)
        mean_1qb_time = gate_dataframe[any_1qb_filter].gate_length.mean()
        var_1qb_time = gate_dataframe[any_1qb_filter].gate_length.var()
        if var_1qb_time > 1e-4:
            print(f"non constant 1 qubit gate time on {prop_dict['backend_name']}")
        record = {
            # qubits physical informations
            "qubit": qubit_num,
            "backend_name": prop_dict["backend_name"],
            "T1 ({})".format(qubit_props_sane["T1"]["unit"]): qubit_props_sane["T1"][
                "value"
            ],
            "T2 ({})".format(qubit_props_sane["T2"]["unit"]): qubit_props_sane["T2"][
                "value"
            ],
            f"Frequency ({qubit_props_sane['frequency']['unit']})": qubit_props_sane[
                "frequency"
            ]["value"],
            f"anharmonicity ({qubit_props_sane['anharmonicity']['unit']})": qubit_props_sane[
                "anharmonicity"
            ][
                "value"
            ],
            "Readout error": qubit_props_sane["readout_error"]["value"],
            "False 0 prob": qubit_props_sane["prob_meas0_prep1"]["value"],
            "False 1 prob": qubit_props_sane["prob_meas1_prep0"]["value"],
            # gates calibrations results
            f"Measurement duration ({qubit_props_sane['readout_length']['unit']})": qubit_props_sane[
                "readout_length"
            ][
                "value"
            ],
            f"One qubit gate time ({gate_dataframe[one_qbit_filters[0]]['gate_time_unit'].tolist()[0]})": mean_1qb_time,
            # "ECR error":ECR_error_entry,
            # f"Two qubits gate time ({gate_dataframe[ecr_gate_filter].gate_time_unit.tolist()[0]})":"pouet",
        }
        for filter in one_qbit_filters:
            filtered_gdf = gate_dataframe[filter]
            gate_name = filtered_gdf.gate.tolist()[0]
            record[f"{gate_name} error"] = filtered_gdf.gate_error.tolist()[0]
            time_entry = filtered_gdf["gate_length"]
            time_unit = filtered_gdf.gate_time_unit.unique()
            assert (
                len(time_unit) == 1
            ), f"mixed time unit in two qubit gate {gate_name} at qubit {qubit_num}. {time_unit}"
            time_unit = time_unit[0]
            record[f"{gate_name} time ({time_unit})"] = time_entry[0]
        for filter in two_qbit_filters:
            filtered_gdf = gate_dataframe[filter]
            error_entry = {
                name: error
                for name, error in zip(filtered_gdf["name"], filtered_gdf["gate_error"])
            }
            gate_name = filtered_gdf.gate.tolist()[0]
            record[f"{gate_name} error"] = error_entry
            time_entry = {
                name: time
                for name, time in zip(filtered_gdf["name"], filtered_gdf["gate_length"])
            }
            time_unit = filtered_gdf.gate_time_unit.unique()
            assert (
                len(time_unit) == 1
            ), f"mixed time unit in two qubit gate {gate_name} at qubit {qubit_num}. {time_unit}"
            time_unit = time_unit[0]
            record[f"{gate_name} time ({time_unit})"] = time_entry

        qubit_records.append(record)
    qubit_dataframe = pd.DataFrame(qubit_records)
    qubit_dataframe.set_index("qubit", inplace=True)
    return (
        qubit_dataframe,
        pd.DataFrame(qubit_only_record),
        gate_dataframe,
        pd.DataFrame(general_dict_list),
    )


# %%
