import string

from InputBase import InputBase

PRIORITY_TABLE = dict(zip(string.ascii_lowercase, range(1, 27)))
PRIORITY_TABLE.update(dict(zip(string.ascii_uppercase, range(27, 53))))

class Input(InputBase):
    def read_task_input(self) -> list:
        stripped = [s.strip() for s in self.raw_input]
        return [(s[:int(len(s) / 2)], s[int(len(s) / 2):]) for s in stripped]


def find_priority(items):
    priority = 0
    for item in items:
        priority += PRIORITY_TABLE[item]
    return priority


def find_common_items(compartments):
    common_items = set(compartments[0]).intersection(compartments[1])
    if len(compartments) > 2:
        for compartment in compartments[2:]:
            common_items = common_items.intersection(compartment)
    return common_items


if __name__ == '__main__':
    task_input = Input('input.txt').read_task_input()

    # part 1
    sum_priorities = 0
    for elf_rucksack in task_input:
        common_items = find_common_items(elf_rucksack)
        sum_priorities += find_priority(common_items)
    print(f'PART1: {sum_priorities}')

    # part 2
    sum_priorities = 0
    for i in range(0, len(task_input), 3):
        group = ["".join(s) for s in task_input[i:i+3]]
        common_items = find_common_items(group)
        sum_priorities += find_priority(common_items)
    print(f'PART2: {sum_priorities}')
