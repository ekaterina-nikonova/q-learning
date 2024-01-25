import numpy as np


class Warehouse:
    def __init__(
        self,
        *,
        width: int = None,
        height: int = None,
    ):
        if width is None:
            width = 4

        if height is None:
            height = 3

        self._width = width
        self._height = height

        self._walls = self.build_walls()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def actions(self):
        return self._walls

    def build_walls(self):
        num_actions = self.width * self.height
        space = np.ones((num_actions, num_actions), np.int8)

        num_of_walls = int(self.width * self.height * 0.25)

        walls_right = np.random.choice(num_actions, num_of_walls, replace=False)
        walls_under = np.random.choice(num_actions, num_of_walls, replace=False)

        walls_right = walls_right[walls_right % self.width != self.width - 1]  # exclude the rightmost column
        walls_under = walls_under[walls_under < (self.width * self.height) - self.width]  # exclude the lowest row

        for wall in walls_right:
            row = wall // self.width
            column = wall % self.width
            if column < self.width - 1:
                from_cell_index = self.width * row + column
                to_cell_index = from_cell_index + 1
                space[from_cell_index][to_cell_index] = 0
                space[to_cell_index][from_cell_index] = 0

        for wall in walls_under:
            row = wall // self.width
            column = wall % self.width
            if row < self.height - 1:
                from_cell_index = self.width * row + column
                to_cell_index = self.width * (row + 1) + column
                space[from_cell_index][to_cell_index] = 0
                space[to_cell_index][from_cell_index] = 0
        return space
