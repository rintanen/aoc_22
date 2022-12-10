from InputBase import InputBase
from typing import Tuple, List
from time import time

class Input(InputBase):
    def read_task_input(self) -> List[str]:
        task_input = [line for line in self.raw_input.split('\n')]
        return task_input


def run_program(task_input, during_these_cycles) -> Tuple[List[int], List[str]]:
    cycle = 1
    x = 1
    program_states: List[int] = []
    crt_rows: List[str] = []
    crt_row = ''
    for instruction in task_input:
        if instruction[4:]:
            # addx instruction
            for _ in range(2):
                # start of cycle -> draw pixel
                crt_row += '#' if len(crt_row) in [x-1, x, x+1] else '.'
                if cycle in during_these_cycles:
                    program_states.append(x)
                cycle += 1
                # new cycle begins here -> if crt row is complete store it and start new one
                if (cycle - 1) % 40 == 0:
                    crt_rows.append(crt_row)
                    crt_row = ''
            x += int(instruction[4:])
        else:
            # noop instruction
            # start of cycle -> draw pixel
            crt_row += '#' if len(crt_row) in [x - 1, x, x + 1] else '.'
            if cycle in during_these_cycles:
                program_states.append(x)
            cycle += 1
            if (cycle - 1) % 40 == 0:
                # new cycle begins here -> if crt row is complete store it and start new one
                crt_rows.append(crt_row)
                crt_row = ''
    return program_states, crt_rows


if __name__ == '__main__':
    task_input = Input('input.txt').read_task_input()
    # return reg state during these cycles
    cycles = [20, 60, 100, 140, 180, 220]
    program_states, crt_rows = run_program(task_input, during_these_cycles=cycles)
    sum_of_signal_powers = sum([x*y for x, y in zip(program_states, cycles)])
    print(f'Part 1: {sum_of_signal_powers}')
    display_image = "\n".join(crt_rows)
    print(f'Part 2:\n {display_image}')
