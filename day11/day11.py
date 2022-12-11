from InputBase import InputBase
import math

class Input(InputBase):
    def read_task_input(self):
        task_input = [line for line in self.raw_input.split('\n\n')]
        task_input = [monkey.split('\n')[1:] for monkey in task_input]
        task_input = [[
            list(map(int, line[0].split(': ')[1].split(', '))),
            eval(f'lambda old: {line[1].split("= ")[1]}'),
            int(line[2].split('by ')[1]),
            (int(line[3].split('monkey ')[1]), int(line[4].split('monkey ')[1]))
        ] for line in task_input]
        return task_input


def keep_away_game(monkeys, rounds, relief: bool, lcm=None):
    items = 0
    worry_adjust_operation = 1
    test_divisible = 2
    throws_to = 3
    monkeys_inspected_times = [0] * len(monkeys)
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            while monkey[items]:
                worry_level = monkey[worry_adjust_operation](monkey[items].pop(0))
                worry_level = worry_level // 3 if relief else worry_level % lcm
                if worry_level % monkey[test_divisible] == 0:
                    monkeys[monkey[throws_to][0]][items].append(worry_level)
                else:
                    monkeys[monkey[throws_to][1]][items].append(worry_level)
                monkeys_inspected_times[i] += 1
    return math.prod(sorted(monkeys_inspected_times)[-2:])


if __name__ == '__main__':
    monkeys = Input('input.txt').read_task_input()
    monkeys_pt2 = Input('input.txt').read_task_input()
    monkey_business = keep_away_game(monkeys, 20, True)
    print(f'Part 1: monkey_business {monkey_business}')

    # find the smallest common multiplier among the modulus test values to scale worry levels
    lest_common_multiplier = math.lcm(*[monkey[2] for monkey in monkeys])
    monkey_business = keep_away_game(monkeys_pt2, 10000, False, lest_common_multiplier)
    print(f'Part 2: monkey_business {monkey_business}')
