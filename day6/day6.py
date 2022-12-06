from InputBase import InputBase
from functools import cached_property
from datetime import datetime

class Input(InputBase):
    def read_task_input(self):
        return self.raw_input


def n_unique(iterable):
    num_unique = len(iterable) - (len(iterable) - len(set(iterable)))
    return num_unique


class DataStreamBuffer:
    def __init__(self, buffer: str):
        self.buffer = buffer

    @cached_property
    def start_of_packet_marker(self):
        return self.start_of_marker(4)

    @cached_property
    def start_of_message_marker(self):
        return self.start_of_marker(14)

    def start_of_marker(self, num_distinct_chars):
        for i in range(num_distinct_chars, len(self.buffer)):
            if n_unique(self.buffer[i-num_distinct_chars:i]) == num_distinct_chars:
                return i


def test_pt1():
    tests = [('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
             ('nppdvjthqldpwncqszvftbrmjlhg', 6),
             ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
             ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)]
    assert all([DataStreamBuffer(test_buffer).start_of_packet_marker == expected_result
               for test_buffer, expected_result in tests])
    print('PART1 TESTS OK')


def test_pt2():
    tests = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
             ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
             ('nppdvjthqldpwncqszvftbrmjlhg', 23),
             ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
             ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)]
    assert all([DataStreamBuffer(test_buffer).start_of_message_marker == expected_result]
               for test_buffer, expected_result in tests)
    print('PART2 TESTS OK')


if __name__ == '__main__':
    start = datetime.now()
    test_pt1()
    test_pt2()

    task_input = Input('input.txt').read_task_input()
    dsb = DataStreamBuffer(task_input)

    print(f'PART 1: {dsb.start_of_packet_marker}')
    print(f'PART 2: {dsb.start_of_message_marker}')

    end = datetime.now()
    print(f'time elapsed: {(end-start).microseconds / 1000}ns')