from InputBase import InputBase
from typing import List


class Input(InputBase):
    def read_task_input(self) -> list:
        task_input: List[List] = []
        for pair in self.raw_input_lines:
            first, second = pair.strip().split(',')
            first = first.split('-')
            second = second.split('-')
            task_input.append([[int(section) for section in first],
                               [int(section) for section in second]])
        return task_input


def fully_contains(pair) -> bool:
    first, second = pair
    if ((first[0] >= second[0] and first[1] <= second[1]) or
       (second[0] >= first[0] and second[1] <= first[1])):
        return True
    return False


def overlaps(pair) -> bool:
    first = list(range(pair[0][0], pair[0][1] + 1))
    second = list(range(pair[1][0], pair[1][1] + 1))
    if any([item in second for item in first]):
        return True
    return False


if __name__ == "__main__":
    fully_contains_count = 0
    overlaps_count = 0
    for pair in Input('input.txt').read_task_input():
        if fully_contains(pair):
            fully_contains_count += 1
        if overlaps(pair):
            overlaps_count += 1

    print(f'PART 1: {fully_contains_count}')
    print(f'PART 2: {overlaps_count}')
