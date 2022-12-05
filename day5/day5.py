from InputBase import InputBase
import re
from typing import List, Tuple


class Input(InputBase):
    def read_task_input(self) -> Tuple[List[str], List[int]]:
        txt = "".join(self.raw_input)
        return self.stacks(txt), self.rearrangements(txt)

    def rearrangements(self, txt: str) -> List[int]:
        txt = txt.split('\nmove')[1:]
        rearrangements = [re.findall(r'\d+', rearrangement) for rearrangement in txt]
        return [[int(s) for s in num_str] for num_str in rearrangements]

    def stacks(self, txt: str) -> List[str]:
        txt = txt.split('\n\n')[0].split('\n')
        stacks = txt[:-1]
        crate_indices = range(1, len(max(stacks, key=len)), 4)
        new_stacks = []
        for i in crate_indices:
            new_stack = ''
            for stack in stacks:
                if len(stack) < i:
                    continue
                new_stack += stack[i]
            new_stacks.append(new_stack.strip())
        return new_stacks


def run(stacks: List[str], rearrangements: List[int], part: int) -> str:
    for how_many, from_this, to_this in rearrangements:
        move_these = stacks[from_this - 1][:how_many]
        if part == 1:
            move_these = "".join(reversed(move_these))
        stacks[to_this - 1] = move_these + stacks[to_this - 1]
        stacks[from_this - 1] = stacks[from_this - 1][how_many:]
    return "".join([s[0] for s in stacks])


if __name__ == '__main__':
    stacks, rearrangements = Input('input.txt').read_task_input()

    print(f'PART 1: {run(stacks.copy(), rearrangements, 1)}')
    print(f'PART 2: {run(stacks.copy(), rearrangements, 2)}')
