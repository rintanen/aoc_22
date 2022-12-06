from InputBase import InputBase
from functools import cached_property


class Input(InputBase):
    def read_task_input(self):
        input_list = ",".join(self.raw_input_lines).split(',\n,')
        items = [[int(item) for item in one_elf_items.split(',')] for one_elf_items in input_list]
        return items


class FoodItems:
    def __init__(self, input_path):
        self.input = Input(input_path)

    @cached_property
    def items(self):
        return self.input.read_task_input()

    @property
    def total_calories(self):
        return [sum(items) for items in self.items]


if __name__ == '__main__':
    food_items = FoodItems('input.txt')
    print(f'PART 1: {max(food_items.total_calories)}')

    max_three = sorted(food_items.total_calories, reverse=True)[:3]
    print(f'PART 2: {sum(max_three)}')
