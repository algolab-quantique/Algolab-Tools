#%%
import unittest

import pathlib
import shelve
from Algolab_tools.convert.IBMQ_to_panda import IBMQ_backend_prop_dict2panda

#%%


#%%


class backendV1_panda_convert_test(unittest.TestCase):
    def test(self):
        # fiddling with paths because unnittest messes with the locality of the test files
        root = pathlib.Path(__file__).parent.resolve()
        path = str(root / pathlib.Path("backend.shlv"))
        # retreiving serialised property of a backend.
        # That's the best i could do. Backend and BackendProperties object are not easily serialized
        with shelve.open(path, "r") as db:
            props = db["0"]
        # Testing that the function run.
        # The other function offered only convert to the data structure used by this.
        # so it's ok.
        a, b, c, d = IBMQ_backend_prop_dict2panda(props)
        return True


#%%

#%%

if __name__ == "main":
    unittest.main()
