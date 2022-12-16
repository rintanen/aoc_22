import re
from InputBase import InputBase
from bisect import insort

MAN_DISTANCE = lambda sx, sy, bx, by: abs(sx-bx) + abs(sy-by)


class Input(InputBase):
    def read_task_input(self):
        return [list(map(int, re.findall('-?[0-9]+', s))) for s in self.raw_input.split('\n')]


def range_at_given_row(pair, row):
    sx, sy, bx, by = pair
    distance = MAN_DISTANCE(sx, sy, bx, by)
    if abs(sy - row) > distance:
        return None
    else:
        delta_y = abs(distance - abs(sy - row))
        return (sx - delta_y, sx + delta_y)


def merge_ranges(ranges):
    index = 0
    for i, range in enumerate(ranges, start=1):
        if ranges[index][1] >= range[0]:
            # if consecutive ranges overlap
            # i.e. r1_0...r2_0...r1_end...r2_end -> overlap if r1_end >= r2_0
            # merge these ranges i.e. ranges[index] = r1_0....max(r1_end/r2_end)
            ranges[index][1] = max(ranges[index][1], range[1])
        else:
            index = index + 1
            ranges[index] = range
    return ranges[0: index + 1]


def cols_without_beacon_by_row(sensor_beacon_pair, row):
    ranges = []
    for pair in sensor_beacon_pair:
        if range_at_row := range_at_given_row(pair, row):
            # append new ranges, bisect insort keeps a sorted order
            insort(ranges, list(range_at_row))
    merged = merge_ranges(ranges)
    return merged


def find_isolated_beacon(sensor_beacon_pairs, search_base):
    for i in range(search_base + 1):
        if len(rows:=cols_without_beacon_by_row(sensor_beacon_pairs, i)) > 1:
            x = (rows[1][0] + rows[0][1]) // 2
            return x, i


if __name__ == '__main__':

    # pt1
    task_input = Input('input.txt').read_task_input()
    row = 2000000
    merged_ranges = cols_without_beacon_by_row(task_input, row)
    res = sum([y-x for x, y in merged_ranges])
    print(f'PT1: columns at row {row} where beacon cannot be {res}')

    # pt2
    x, y = find_isolated_beacon(task_input, 56000011)
    tuning_freq = 4000000 * x + y
    print(f'PT2: tuning freq {tuning_freq}')