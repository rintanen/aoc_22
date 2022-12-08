from InputBase import InputBase
import numpy as np
from typing import List
from datetime import datetime


class Input(InputBase):
    def read_task_input(self):
        return np.array([[int(n) for n in row] for row in self.raw_input.split('\n')])


def how_many_visible(tree, grid):
    visible_map = np.where(np.less_equal(tree, grid) == True)[0]
    if visible_map.size >= 1:
        return visible_map[0] + 1
    else:
        return len(grid)


def calc_scenic_score(grid, i, j):
    tree = grid[i, j]
    visible_top = how_many_visible(tree, np.flip(grid[:i, j]))
    visible_left = how_many_visible(tree, np.flip(grid[i, :j]))
    visible_below = how_many_visible(tree, grid[i+1:, j])
    visible_right = how_many_visible(tree, grid[i, j+1:])
    return visible_top * visible_left * visible_below * visible_right


def visible(grid, i, j):
    tree = grid[i, j]
    visible_top = np.greater(tree, grid[:i, j]).all()
    visible_left = np.greater(tree, grid[i, :j]).all()
    visible_below = np.greater(tree, grid[i+1:, j]).all()
    visible_right = np.greater(tree, grid[i, j+1:]).all()
    return any([visible_top, visible_left, visible_below, visible_right])


def calculate_visible_trees(tree_grid: List[int]) -> int:
    rows, columns = tree_grid.shape
    visible_count = 0
    highest_scenic_score = 0
    for row_ind in list(range(1, rows - 1)):
        for tree_ind in list(range(1, columns - 1)):
            # PT1
            if visible(tree_grid, row_ind, tree_ind):
                visible_count += 1
            # PT2
            scenic_score = calc_scenic_score(tree_grid, row_ind, tree_ind)

            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return visible_count + 2 * rows + 2 * columns - 4, highest_scenic_score


def test():
    test_input = '30373\n25512\n65332\n33549\n35390'
    test_input = np.array([[int(n) for n in row] for row in test_input.split('\n')])
    n_visible_trees, highest_scenic_score = calculate_visible_trees(test_input)
    assert n_visible_trees == 21
    assert highest_scenic_score == 8


if __name__ == '__main__':
    test()
    start = datetime.now()
    task_input = Input('input.txt').read_task_input()
    visible_trees, highest_scenic_score = calculate_visible_trees(task_input)
    end = datetime.now()
    print(f'PART 1: {visible_trees}')
    print(f'PART 2: {highest_scenic_score}')
    print(f'time elapsed: {(end - start).microseconds // 1000}ns')
