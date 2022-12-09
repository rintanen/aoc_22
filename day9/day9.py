from InputBase import InputBase
from typing import Tuple, List
from time import time

class Input(InputBase):
    def read_task_input(self) -> List[Tuple[str, int]]:
        task_input = [line for line in self.raw_input.split('\n')]
        task_input = [line.split() for line in task_input]
        task_input = [(knot, int(moves_this_amount)) for knot, moves_this_amount in task_input]
        return task_input


class Head:
    mark = {'U': 1,
            'L': -1,
            'R': 1,
            'D': -1}

    def __init__(self, x_init: int = 0, y_init: int = 0):
        self.x = x_init
        self.y = y_init
        self.location_history = [(x_init, y_init)]

    @property
    def location(self) -> tuple[int, int]:
        return self.x, self.y

    def moves(self, direction: str, amount: int):
        if direction in ['L', 'R']:
            self.x += self.mark[direction] * amount
        elif direction in ['U', 'D']:
            self.y += self.mark[direction] * amount
        self.location_history.append(self.location)

class Tail(Head):
    def moves(self, previous):
        dx = previous.x - self.x
        dy = previous.y - self.y
        is_adjacent = abs(dx) <= 1 and abs(dy) <= 1
        if not is_adjacent:
            if abs(dx) >= 1:
                self.x += int(dx / abs(dx))
            if abs(dy) >= 1:
                self.y += int(dy / abs(dy))
        self.location_history.append(self.location)


def play(task_input, knots) -> int:
    def update_tails_locations(head: Head, tails: List[Tail]):
        tails[0].moves(previous=head)
        for i in range(1, len(tails)):
            tails[i].moves(previous=tails[i - 1])

    head = Head()
    tails: List[Tail] = []
    for i in range(knots - 1):
        tails.append(Tail())

    for direction, amount in task_input:
        for i, step in enumerate([1] * amount, start=1):
            head.moves(direction=direction, amount=step)
            update_tails_locations(head, tails)
    return len(set(tails[-1].location_history))


if __name__ == '__main__':
    task_input = Input('input.txt').read_task_input()
    start = time()
    print(f'PART 1: {play(task_input, 2)}')
    print(f'PART 2: {play(task_input, 10)}')
    end = time()
    print(f'Elapsed {round((end-start) * 1000)}ms')