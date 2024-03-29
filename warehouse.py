import numpy as np

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


class Warehouse:
    def __init__(
        self,
        *,
        width: int = None,
        height: int = None,
        num_of_walls: int = None,
    ):
        if width is None:
            width = 4

        if height is None:
            height = 3

        self._width = width
        self._height = height

        if num_of_walls is None:
            self.num_of_walls = int(self.width * self.height * 0.25)
        else:
            self.num_of_walls = num_of_walls

        self._actions = self.build_actions()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def actions(self):
        return self._actions

    def build_actions(self):
        num_actions = self.width * self.height
        space = np.zeros((num_actions, num_actions), np.int8)

        for position in range(num_actions):
            above = position - self.width
            below = position + self.width
            left = position - 1
            right = position + 1

            if above > 0:  # not the first row
                space[position][above] = 1
                space[above][position] = 1

            if below < num_actions:  # not the last row
                space[position][below] = 1
                space[below][position] = 1

            if position % self.width != 0:  # not the first column
                space[position][left] = 1
                space[left][position] = 1

            if position % self.width != self.width - 1:  # not the last column
                space[position][right] = 1
                space[right][position] = 1

        walls_right = np.random.choice(num_actions, self.num_of_walls, replace=False)
        walls_under = np.random.choice(num_actions, self.num_of_walls, replace=False)

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
        fig, ax = plt.subplots(1, 1, tight_layout=True)
        plt.xticks([])
        plt.yticks([])
        for x in range(self.width * self.height):
            for y in range(self.width * self.height):
                if not self.actions[x][y]:
                    row = x // self.width
                    col = x % self.width
                    if y - x == 1:
                        self.draw_right(ax, row, col)
                    elif y - x == self.width:
                        self.draw_under(ax, row, col)

        for cell_num in range(self.width * self.height):
            row = cell_num // self.width
            col = cell_num % self.width
            x = col + 0.5
            y = (self.height - row) - 0.5
            font = FontProperties()
            font.set_size(fig.bbox.xmax / (self.width * 5))
            alignment = {'horizontalalignment': 'center', 'verticalalignment': 'center'}
            plt.text(x, y, str(cell_num), fontproperties=font, **alignment)
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
            xmin=x_min / self.width,
            xmax=x_max / self.width,
        )

