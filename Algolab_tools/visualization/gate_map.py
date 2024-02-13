"""A module for visualizing device coupling maps"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

#%
# fmt: off
# No one gives a crap about reading this.
# It should be generated programmatically, not hardcoded like that. IBM's quality code!
qubit_coordinates_map = {}

qubit_coordinates_map[1] = [[0, 0]]

qubit_coordinates_map[5] = [[1, 0], [0, 1], [1, 1], [1, 2], [2, 1]]

qubit_coordinates_map[7] = [[0, 0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]

qubit_coordinates_map[20] = [[0, 0],[0, 1],[0, 2],[0, 3],[0, 4],[1, 0],[1, 1],[1, 2],[1, 3],[1, 4],[2, 0],[2, 1],[2, 2],[2, 3],[2, 4],[3, 0],[3, 1],[3, 2],[3, 3],[3, 4]]

qubit_coordinates_map[15] = [[0, 0],[0, 1],[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[1, 7],[1, 6],[1, 5],[1, 4],[1, 3],[1, 2],[1, 1],[1, 0]]

qubit_coordinates_map[16] = [[1, 0],[1, 1],[2, 1],[3, 1],[1, 2],[3, 2],[0, 3],[1, 3],[3, 3],[4, 3],[1, 4],[3, 4],[1, 5],[2, 5],[3, 5],[1, 6]]

qubit_coordinates_map[27] = [[1, 0],[1, 1],[2, 1],[3, 1],[1, 2],[3, 2],[0, 3],[1, 3],[3, 3],[4, 3],[1, 4],[3, 4],[1, 5],[2, 5],[3, 5],[1, 6],[3, 6],[0, 7],[1, 7],[3, 7],[4, 7],[1, 8],[3, 8],[1, 9],[2, 9],[3, 9],[3, 10]]

qubit_coordinates_map[28] = [[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[1, 2],[1, 6],[2, 0],[2, 1],[2, 2],[2, 3],[2, 4],[2, 5],[2, 6],[2, 7],[2, 8],[3, 0],[3, 4],[3, 8],[4, 0],[4, 1],[4, 2],[4, 3],[4, 4],[4, 5],[4, 6],[4, 7],[4, 8]]

qubit_coordinates_map[53] = [[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[1, 2],[1, 6],[2, 0],[2, 1],[2, 2],[2, 3],[2, 4],[2, 5],[2, 6],[2, 7],[2, 8],[3, 0],[3, 4],[3, 8],[4, 0],[4, 1],[4, 2],[4, 3],[4, 4],[4, 5],[4, 6],[4, 7],[4, 8],[5, 2],[5, 6],[6, 0],[6, 1],[6, 2],[6, 3],[6, 4],[6, 5],[6, 6],[6, 7],[6, 8],[7, 0],[7, 4],[7, 8],[8, 0],[8, 1],[8, 2],[8, 3],[8, 4],[8, 5],[8, 6],[8, 7],[8, 8],[9, 2],[9, 6]]

qubit_coordinates_map[65] = [[0, 0],[0, 1],[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[0, 7],[0, 8],[0, 9],[1, 0],[1, 4],[1, 8],[2, 0],[2, 1],[2, 2],[2, 3],[2, 4],[2, 5],[2, 6],[2, 7],[2, 8],[2, 9],[2, 10],[3, 2],[3, 6],[3, 10],[4, 0],[4, 1],[4, 2],[4, 3],[4, 4],[4, 5],[4, 6],[4, 7],[4, 8],[4, 9],[4, 10],[5, 0],[5, 4],[5, 8],[6, 0],[6, 1],[6, 2],[6, 3],[6, 4],[6, 5],[6, 6],[6, 7],[6, 8],[6, 9],[6, 10],[7, 2],[7, 6],[7, 10],[8, 1],[8, 2],[8, 3],[8, 4],[8, 5],[8, 6],[8, 7],[8, 8],[8, 9],[8, 10]]

qubit_coordinates_map[127] = [[0, 0],[0, 1],[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[0, 7],[0, 8],[0, 9],[0, 10],[0, 11],[0, 12],[0, 13],[1, 0],[1, 4],[1, 8],[1, 12],[2, 0],[2, 1],[2, 2],[2, 3],[2, 4],[2, 5],[2, 6],[2, 7],[2, 8],[2, 9],[2, 10],[2, 11],[2, 12],[2, 13],[2, 14],[3, 2],[3, 6],[3, 10],[3, 14],[4, 0],[4, 1],[4, 2],[4, 3],[4, 4],[4, 5],[4, 6],[4, 7],[4, 8],[4, 9],[4, 10],[4, 11],[4, 12],[4, 13],[4, 14],[5, 0],[5, 4],[5, 8],[5, 12],[6, 0],[6, 1],[6, 2],[6, 3],[6, 4],[6, 5],[6, 6],[6, 7],[6, 8],[6, 9],[6, 10],[6, 11],[6, 12],[6, 13],[6, 14],[7, 2],[7, 6],[7, 10],[7, 14],[8, 0],[8, 1],[8, 2],[8, 3],[8, 4],[8, 5],[8, 6],[8, 7],[8, 8],[8, 9],[8, 10],[8, 11],[8, 12],[8, 13],[8, 14],[9, 0],[9, 4],[9, 8],[9, 12],[10, 0],[10, 1],[10, 2],[10, 3],[10, 4],[10, 5],[10, 6],[10, 7],[10, 8],[10, 9],[10, 10],[10, 11],[10, 12],[10, 13],[10, 14],[11, 2],[11, 6],[11, 10],[11, 14],[12, 1],[12, 2],[12, 3],[12, 4],[12, 5],[12, 6],[12, 7],[12, 8],[12, 9],[12, 10],[12, 11],[12, 12],[12, 13],[12, 14]]
# fmt: on

#%%
def _set_defaults(defaults_dict, defaults):
    for key, value in defaults:
        if key not in defaults_dict:
            defaults_dict[key] = value
    return defaults_dict


def gate_map(gate_dataframe, nqubits_full: int, qubit_subset=None, **kwargs):
    """
    construct the gate map of the qubitsubset from the gate dataframe.
    number of qubits is used to select the suitable qubit coordinates.
    No supplied qubit_subset means all qubit are displayed.
    number of qubit could be guessed...
    """
    defaults = [
        ("font_size", 6),
        ("font_color", "w"),
        ("font_weight", "bold"),
        ("font_family", "sans-serif"),
        ("node_size", 210),
        ("node_color", "b"),
        ("node_outline_color", "k"),
        ("edge_color", "b"),
        ("edge_outline_color", "k"),
        ("edge_border_width", 2),
        ("edge_width", 6),
    ]
    kwargs = _set_defaults(kwargs, defaults)
    G, subset_coordinate, coupling_gates = gate_graph(
        gate_dataframe, nqubits_full, qubit_subset
    )
    nx.draw_networkx_nodes(
        G,
        subset_coordinate,
        node_size=kwargs["node_size"],
        node_color=kwargs["node_color"],
        edgecolors=kwargs["node_outline_color"],
    )
    nx.draw_networkx_edges(
        G,
        subset_coordinate,
        width=kwargs["edge_border_width"] + kwargs["edge_width"],
        edge_color=kwargs["edge_outline_color"],
    )  # Serves to create a black outline to the edges
    nx.draw_networkx_edges(G, subset_coordinate, width=7, edge_color="b")
    # nx.draw(G, subset_coordinate, node_color='b', edge_color='b', width=10.0,edgecolors='black')
    nx.draw_networkx_labels(
        G,
        subset_coordinate,
        font_size=kwargs["font_size"],
        font_family=kwargs["font_family"],
        font_weight=kwargs["font_weight"],
        font_color=kwargs["font_color"],
    )


def gate_graph(gate_dataframe, nqubits_full: int, qubit_subset=None):
    """
    Filter the supplied dataframe to extract the couling gate information of the
    desired qubits subset.
    Prepares a networkx graphs, and coordinates dictionnary for the nodes of of the graph.
    Arguments:
        gate dataframe, e.g. output of
    return (graph,coordinates,filtered dataframe)
    """
    if not qubit_subset:
        qubit_subset = np.arange(nqubits_full)
    coupling_gates = gate_dataframe[
        (
            gate_dataframe["qubits"].apply(
                lambda x: len(x) == 2 and x[0] in qubit_subset and x[1] in qubit_subset
            )
        )
    ]
    qubits_coordinate = np.array(qubit_coordinates_map[nqubits_full])

    def ibm_standard_orientation(pair):
        return np.array([[0, 1], [-1, 0]]) @ pair

    subset_coordinate = {
        qubit: ibm_standard_orientation(qubits_coordinate[qubit])
        for qubit in qubit_subset
    }
    G = nx.Graph()
    for coupled_qubits in coupling_gates["qubits"]:
        G.add_edge(*coupled_qubits)
    return G, subset_coordinate, coupling_gates


gate_map(gates, 127)
plt.savefig("test.pdf")
# %%
import shelve
import pathlib
from Algolab_tools.convert.IBMQ_to_panda import IBMQ_backend_prop_dict2panda

root = pathlib.Path(__file__).parent.parent.parent.resolve()
path = str(root / pathlib.Path("tests/backend.shlv"))
print(path)
#%%
# retreiving serialised property of a backend.
# That's the best i could do. Backend and BackendProperties object are not easily serialized
with shelve.open(path, "r") as db:
    props = db["0"]

exerpt, qubit, gates, other = IBMQ_backend_prop_dict2panda(props)
gates
qubit_subset = np.arange(127)
coupling_gates = gates[
    (
        gates["qubits"].apply(
            lambda x: len(x) == 2 and x[0] in qubit_subset and x[1] in qubit_subset
        )
    )
]
for x in coupling_gates["qubits"]:
    print(x)
#%%
# %%
# %%
import numpy as np

G = nx.path_graph(20)  # An example graph
center_node = 5  # Or any other node to be in the center
edge_nodes = set(G) - {center_node}
# Ensures the nodes around the circle are evenly distributed
pos = nx.circular_layout(G.subgraph(edge_nodes))
pos[center_node] = np.array([0, 0])  # manually specify node position
nx.draw(G, pos, with_labels=True)
# %%
edges = coupling_gates["qubits"].tolist()
edges
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(3, 4)
G.add_edge(1, 5)
G.add_edge(3, 5)
nx.draw(
    G,
    pos,
    node_color="b",
    edgelist=edges,
    edge_color=weights,
    width=10.0,
    edge_cmap=plt.cm.Blues,
)
nx.draw(G)


# %% exemple Tania
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Plot graph
G = nx.Graph()
G.add_edge(0, 1, weight=3.0)
G.add_edge(1, 2, weight=1.0)
G.add_edge(2, 3, weight=6.0)
G.add_edge(3, 4, weight=1.0)
G.add_edge(4, 5, weight=3.0)
G.add_edge(5, 0, weight=9.0)
pos = nx.spring_layout(G, seed=7)
edge_labels = nx.get_edge_attributes(G, "weight")
viridis = mpl.colormaps["viridis"].resampled(6)
for i, color in enumerate(viridis.colors):
    nx.draw_networkx_nodes(G, pos, nodelist=[i], node_size=400, node_color=color)
    nx.draw_networkx_edges(
        G, pos, width=2, edgelist=[(i, (i + 1) % 6)], edge_color=color
    )
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_color="w")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()


# %%
