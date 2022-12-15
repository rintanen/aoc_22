from InputBase import InputBase
from functools import cached_property
import numpy as np

class Input(InputBase):
    def read_task_input(self):
        return [s.split(' -> ') for s in self.raw_input.split('\n')]


class Grid():
    def __init__(self, scan, infinity_mode=False):
        self.infinity_mode = infinity_mode
        self.v, self.h = self.create_vectors(scan)
        self.grid = self.init_grid()

    @cached_property
    def vertical(self):
        d = {}
        for x, y1, y2 in self.v:
            if x not in d.keys():
                d[x] = list(range(y1, y2+1))
            else:
                d[x] = list(set(d[x] + list(range(y1, y2+1))))
        return d

    @cached_property
    def horizontal(self):
        d = {}
        for y, x1, x2 in self.h:
            if y not in d.keys():
                d[y] = list(range(x1, x2+1))
            else:
                d[y] = list(set(d[y] + list(range(x1, x2+1))))
        if self.infinity_mode:
            floor_level = max(list(d.keys())) + 2
            d[floor_level] = list(range(500-floor_level+1, 500+floor_level))
        return d

    @cached_property
    def x_limits(self):
        minimum = min(self.horizontal[list(self.horizontal.keys())[0]])
        maximum = 0
        for key, items in self.horizontal.items():
            if min(items) < minimum:
                minimum = min(items)
            if max(items) > maximum:
                maximum = max(items)
        return minimum, maximum

    @cached_property
    def vertical_mapping(self):
        return dict(zip(range(self.x_limits[0], self.x_limits[1] + 1),
                        range(0, self.x_limits[1] - self.x_limits[0] + 1)))

    @property
    def sand_drop_location(self):
        return (0, self.vertical_mapping[500])

    def init_grid(self):
        y_min, y_max = 0, len(range(0, max(list(self.horizontal.keys())) + 1))
        grid = np.zeros(shape=(y_max - y_min, self.x_limits[1] - self.x_limits[0] + 1), dtype=int)
        for key, items in self.horizontal.items():
            mapped = [self.vertical_mapping[item] for item in items]
            grid[key, mapped] = 1
        for key, items in self.vertical.items():
            grid[items, self.vertical_mapping[key]] = 1
        return grid

    @staticmethod
    def create_vectors(scan):
        vertical = []
        lateral = []
        for line in scan:
            prev = line[0].split(',')
            for coord in line[1:]:
                coord = coord.split(',')
                if coord[0] == prev[0]:
                    vertical.append((int(prev[0]), int(min([prev[1], coord[1]])), int(max([prev[1], coord[1]]))))
                elif coord[1] == prev[1]:
                    lateral.append((int(coord[1]), int(min([prev[0], coord[0]])), int(max([prev[0], coord[0]]))))
                prev = coord
        return vertical, lateral


class SandPhysicsSimulation:
    def __init__(self, grid: Grid):
        self.grid = grid

    def forward(self):
        # start dropping sand
        while self._sand_drop(self.grid.sand_drop_location):
            pass
        return self.grid.grid[self.grid.grid == 2].size

    def _sand_drop(self, sand_loc):
        # edge check
        if sand_loc[1] < 0 or sand_loc[1] > self.grid.grid.shape[1] - 1:
            return False
        # check if sand is falling to abyss (pt1)
        if np.all(self.grid.grid[sand_loc[0]+1:, sand_loc[1]] == 0):
            return False

        if self.grid.grid[sand_loc] == 2:
            # sand has finally reached the roof (pt2)
            return False

        self.grid.grid[sand_loc] = 2

        if self.grid.grid[sand_loc[0] + 1, sand_loc[1]] == 0:
            self.grid.grid[sand_loc] = 0
            return self._sand_drop((sand_loc[0] + 1, sand_loc[1]))
        elif self.grid.grid[sand_loc[0] + 1, sand_loc[1]] in [1, 2]:
            if self.grid.grid[sand_loc[0] + 1, sand_loc[1] - 1] == 0:
                self.grid.grid[sand_loc] = 0
                return self._sand_drop((sand_loc[0] + 1, sand_loc[1] - 1))
            if sand_loc[1] == self.grid.grid.shape[1] - 1:
                # pt2 requires this check to see when sand is at the right edge
                return True
            if self.grid.grid[sand_loc[0] + 1, sand_loc[1] + 1] == 0:
                self.grid.grid[sand_loc] = 0
                return self._sand_drop((sand_loc[0] + 1, sand_loc[1] + 1))
        if (self.grid.grid[sand_loc[0] + 1, sand_loc[1] - 1] in [1, 2] and
           self.grid.grid[sand_loc[0] + 1, sand_loc[1] + 1] in [1, 2]):
            return True


def test():
    scan = '498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9'.split('\n')
    scan = [s.split(' -> ') for s in scan]

    simulation = SandPhysicsSimulation(grid=Grid(scan))
    sands_dropped = simulation.forward()
    assert sands_dropped == 24
    print('TEST PT1 OK')
    print(f'{sands_dropped} units of sand dropped')

    new_simulation = SandPhysicsSimulation(grid=Grid(scan, infinity_mode=True))
    sands_dropped = new_simulation.forward()
    assert sands_dropped == 93
    print('TEST PT2 OK')
    print(f'{sands_dropped} units of sand dropped')


if __name__ == '__main__':
    test()

    # pt1
    scan = Input('input.txt').read_task_input()
    simulation = SandPhysicsSimulation(grid=Grid(scan))
    sands_dropped = simulation.forward()
    print(f'Part 1: {sands_dropped} units of sand dropped')

    # pt2
    new_simulation = SandPhysicsSimulation(grid=Grid(scan, infinity_mode=True))
    sands_dropped = new_simulation.forward()
    print(f'Part 2: {sands_dropped} units of sand dropped')
