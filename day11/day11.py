from InputBase import InputBase
from typing import List, Callable
from functools import reduce
import operator


class Input(InputBase):
    def read_task_input(self) -> List[str]:
        task_input = [line for line in self.raw_input.split('\n\n')]
        task_input = [monkey.split('\n') for monkey in task_input]
        return task_input


class Monkey:
    def __init__(self, uid: int, items: list[int], worry_adjust_operation: Callable, worry_adjust_value: int,
                 division_test_value: int, throw_to_options: tuple):
        self.uid = uid
        self.items = items
        self.worry_adjust_operation = worry_adjust_operation
        self.worry_adjust_value = worry_adjust_value
        self.division_test_value = division_test_value
        self.throw_to_options = throw_to_options
        self.inspected_times = 0

    def observes(self) -> int:
        worry_level = reduce(self.worry_adjust_operation, [self.items.pop(0), self.worry_adjust_value])
        self.inspected_times += 1
        return worry_level

    def catches(self, item):
        self.items.append(item)

    def throws_to(self, worry_level) -> int:
        if worry_level % self.division_test_value == 0:
            throw_to = self.throw_to_options[0]
        else:
            throw_to = self.throw_to_options[1]
        return throw_to


def create_monkey(monkey_info):
    monkey_uid = int(monkey_info[0][:-1][7:])
    starting_items = [int(item) for item in monkey_info[1].split(': ')[1].split(', ')]
    add_or_multiply = '+' if '+' in monkey_info[2] else '*'
    worry_adjust_value = monkey_info[2].split(add_or_multiply)[1].strip()

    if worry_adjust_value == 'old':
        worry_adjust_value = 2
        worry_adjust_operation = operator.pow
    else:
        worry_adjust_value = int(worry_adjust_value)
        worry_adjust_operation = operator.add if add_or_multiply == '+' else operator.mul

    division_test_value = int(monkey_info[3].split('by ')[1])
    throw_to_options = (int(monkey_info[4].split('monkey ')[1]), int(monkey_info[5].split('monkey ')[1]))
    return Monkey(uid=monkey_uid,
                  items=starting_items,
                  worry_adjust_operation=worry_adjust_operation,
                  worry_adjust_value=worry_adjust_value,
                  division_test_value=division_test_value,
                  throw_to_options=throw_to_options)


def keep_away_game(monkeys, rounds, relief: bool = False) -> int:
    current_monkey = monkeys[0]
    game_round = 1
    while game_round <= rounds:
        while current_monkey.items:
            worry_level = current_monkey.observes()
            worry_level = worry_level // 3 if relief else worry_level
            throws_to = current_monkey.throws_to(worry_level)
            monkeys[throws_to].catches(worry_level)
        if monkeys.index(current_monkey) + 1 == len(monkeys):
            current_monkey = monkeys[0]
            game_round += 1
        else:
            current_monkey = monkeys[monkeys.index(current_monkey) + 1]
    monkey_business = reduce(operator.mul, sorted([monkey.inspected_times for monkey in monkeys])[-2:])
    return monkey_business


if __name__ == '__main__':
    task_input = Input('input.txt').read_task_input()
    monkeys: List[Monkey] = []
    for monkey_info in task_input:
        monkeys.append(create_monkey(monkey_info))

    monkey_business = keep_away_game(monkeys, rounds=20, relief=True)
    print(f'Part 1: level of monkey business is {monkey_business}')
