from unittest import TestCase

import numpy as np

from warehouse import Warehouse


class TestWarehouse(TestCase):
    def test_space_symmetrical(self):
        warehouse = Warehouse(width=5, height=4)
        self.assertTrue(np.allclose(warehouse.actions, warehouse.actions.T))

    def test_number_of_actions(self):
        warehouse = Warehouse(width=15, height=14, num_of_walls=0)
        actions_4 = (warehouse.width - 2) * (warehouse.height - 2)
        actions_3 = 2 * (warehouse.width - 2) + 2 * (warehouse.height - 2)
        actions_2 = 4
        num_of_actions_expected = actions_4 * 4 + actions_3 * 3 + actions_2 * 2
        num_of_actions_actual = np.count_nonzero(warehouse.actions)
        self.assertEqual(num_of_actions_actual, num_of_actions_expected)

    def test_draw(self):
        warehouse = Warehouse(width=15, height=14)
        warehouse.draw()
