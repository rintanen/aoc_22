from InputBase import InputBase
import numpy as np
from typing import List, Tuple
from datetime import datetime


class Input(InputBase):
    def read_task_input(self):
        return np.array([[int(n) for n in row] for row in self.raw_input.split('\n')])


def how_many_visible(tree, trees_in_one_direction):
    # indices of trees that taller or equal than the tree we examine
    visible_map = np.where(np.less_equal(tree, trees_in_one_direction) == True)[0]
    if visible_map.size >= 1:
        # return the index of first such tree (plus 1 because the first view blocking tree also counts)
        return visible_map[0] + 1
    else:
        # if none are taller than or equal return the number of trees in that direction
        return len(trees_in_one_direction)


def calc_scenic_score(forest: np.ndarray, i: int, j: int) -> int:
    # i: row
    # j: column
    tree = forest[i, j]
    visible_top = how_many_visible(tree, np.flip(forest[:i, j]))
    visible_left = how_many_visible(tree, np.flip(forest[i, :j]))
    visible_below = how_many_visible(tree, forest[i + 1:, j])
    visible_right = how_many_visible(tree, forest[i, j + 1:])
    return visible_top * visible_left * visible_below * visible_right


def visible(forest: np.ndarray, i: int, j: int) -> bool:
    # i: row
    # j: column
    tree = forest[i, j]
    # True if all trees in given direction are taller than the one we examine
    visible_top = np.greater(tree, forest[:i, j]).all()
    visible_left = np.greater(tree, forest[i, :j]).all()
    visible_below = np.greater(tree, forest[i + 1:, j]).all()
    visible_right = np.greater(tree, forest[i, j + 1:]).all()
    return any([visible_top, visible_left, visible_below, visible_right])


def calculate_visible_trees(forest: List[int]) -> Tuple[int, int]:
    rows, columns = forest.shape
    visible_count = 0
    highest_scenic_score = 0
    # loop through all trees except ones on the edge of forest
    for row_ind in list(range(1, rows - 1)):
        for tree_ind in list(range(1, columns - 1)):
            # PT1
            if visible(forest, row_ind, tree_ind):
                visible_count += 1
            # PT2
            scenic_score = calc_scenic_score(forest, row_ind, tree_ind)

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
