import numpy as np

from matplotlib import pyplot as plt


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

    def draw(self,):
        # plt.figure(figsize=(self.width, self.height))
        fig, ax = plt.subplots(1, 1, tight_layout=True)
        for x in range(self.width * self.height):
            for y in range(self.width * self.height):
                if not self.actions[x][y]:
                    row = x // self.width
                    col = x % self.width
                    if y - x == 1:
                        self.draw_right(ax, row, col)
                    elif y - x == self.width:
                        self.draw_under(ax, row, col)
        plt.xlim([0, self.width])
        plt.ylim([0, self.height])
        plt.show()

    def draw_right(self, ax, row, col):
        y_min = (self.height - row - 1)
        y_max = (self.height - row)
        x = col + 1
        ax.axvline(
            x,
            lw=2,
            ymin=y_min / self.height,
            ymax=y_max / self.height,
        )

    def draw_under(self, ax, row, col):
        x_min = col
        x_max = x_min + 1
        ax.axhline(
            self.height - (row + 1),
            lw=2,
            c='r',
            xmin=x_min / self.width,
            xmax=x_max / self.width,
        )

