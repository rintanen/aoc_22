from InputBase import InputBase
import re


class Input(InputBase):
    def read_task_input(self) -> tuple[list[str], list[int]]:
        txt = "".join(self.raw_input)
        return self.stacks(txt), self.rearrangements(txt)

    def rearrangements(self, txt: str) -> list[int]:
        txt = txt.split('\nmove')[1:]
        rearrangements = [re.findall(r'\d+', rearrangement) for rearrangement in txt]
        return [[int(s) for s in num_str] for num_str in rearrangements]

    def stacks(self, txt: str) -> list[str]:
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


def run(stacks: list[str], rearrangements: list[int], part: int) -> str:
    for move_this, from_this, to_this in rearrangements:
        if part == 1:
            stacks[to_this - 1] = "".join(reversed(stacks[from_this - 1][:move_this])) + stacks[to_this - 1]
        elif part == 2:
            stacks[to_this - 1] = stacks[from_this - 1][:move_this] + stacks[to_this - 1]
        stacks[from_this - 1] = stacks[from_this - 1][move_this:]
    return "".join([s[0] for s in stacks])


if __name__ == '__main__':
    stacks, rearrangements = Input('input.txt').read_task_input()

    print(f'PART 1: {run(stacks.copy(), rearrangements, 1)}')
    print(f'PART 2: {run(stacks.copy(), rearrangements, 2)}')
