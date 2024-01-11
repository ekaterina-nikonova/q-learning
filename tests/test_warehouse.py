from unittest import TestCase

import numpy as np

from warehouse import Warehouse


class TestWarehouse(TestCase):
    def test_space_symmetrical(self):
        warehouse = Warehouse(width=5, height=4)
        self.assertTrue(np.allclose(warehouse.actions, warehouse.actions.T))
