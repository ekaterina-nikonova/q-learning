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

        # Walk the space from left to right, top to bottom and randomly insert walls
        # to the right and down from the current cell.
        for row in range(self.height - 1):
            for column in range(self.width - 1):
                right = np.random.randint(1) if column < self.width - 1 else 1
                down = np.random.randint(1) if row < self.height - 1 else 1

                if not right:
                    from_cell_index = self.width * row + column
                    to_cell_index = from_cell_index + 1
                    space[from_cell_index][to_cell_index] = 0
                    space[to_cell_index][from_cell_index] = 0

                if not down:
                    from_cell_index = self.width * row + column
                    to_cell_index = self.width * (row + 1) + column
                    space[from_cell_index][to_cell_index] = 0
                    space[to_cell_index][from_cell_index] = 0
        return space
