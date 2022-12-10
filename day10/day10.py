from InputBase import InputBase
from typing import Tuple, List

class Input(InputBase):
    def read_task_input(self) -> List[str]:
        task_input = [line for line in self.raw_input.split('\n')]
        return task_input


def run_program(task_input, during_these_cycles) -> Tuple[List[int], List[str]]:
    cpu_cycle = 1
    x = 1  # register value
    register_values: List[int] = []
    display_rows: List[str] = []
    display_row = ''

    def instruction_routine(n: int):
        nonlocal cpu_cycle, register_values, display_rows, display_row
        for _ in range(n):
            # start of cycle -> draw pixel
            display_row += '#' if len(display_row) in [x - 1, x, x + 1] else '.'
            if cpu_cycle in during_these_cycles:
                register_values.append(x)
            cpu_cycle += 1
            # new cycle begins here -> if crt row is complete store it and start new one
            if (cpu_cycle - 1) % 40 == 0:
                display_rows.append(display_row)
                display_row = ''

    for instruction in task_input:
        if instruction[4:]:
            # addx
            instruction_routine(n=2)
            x += int(instruction[4:])
        else:
            # noop
            instruction_routine(n=1)

    return register_values, display_rows


if __name__ == '__main__':
    task_input = Input('input.txt').read_task_input()
    # return reg state during these cycles
    cycles = [20, 60, 100, 140, 180, 220]
    register_values, display_rows = run_program(task_input, during_these_cycles=cycles)
    sum_of_signal_powers = sum([x * y for x, y in zip(register_values, cycles)])
    print(f'Part 1: {sum_of_signal_powers}')
    display_image = "\n".join(display_rows)
    print(f'Part 2:\n {display_image}')
