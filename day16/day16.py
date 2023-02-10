from InputBase import InputBase
from parse import parse
from functools import cached_property
import sys


class Input(InputBase):
    def read_task_input(self):
        return self.raw_input


class ValveShit:
    def __init__(self, raw_input):
        self.graph, self.flow = self._parse_input(raw_input)
        self.all_valves = list(self.graph.keys())

    @staticmethod
    def _parse_input(raw_input):
        graph = {}
        flow = {}
        for line in raw_input.split('\n'):
            split_strs = (' to valves ', ' tunnels lead') if 'valves' in line else (' to valve ', ' tunnel leads')
            begin, neighbours = line.split(split_strs[0])
            valve, flow_rate = parse("Valve {} has flow rate={:d};" + split_strs[1], begin)
            graph[valve] = neighbours.split(', ')
            flow[valve] = flow_rate
        return graph, flow

    @cached_property
    def valves_with_non_zero_flow_rate(self):
        predicate = lambda x: x > 0
        return {key: value for key, value in self.flow.items() if predicate(value)}

    def graph_list(self):
        inf = sys.maxsize
        graph_list = []
        vertices = list(self.graph.keys())
        for vertix, neighbours in self.graph.items():
            row = [inf] * len(self.graph)
            row[vertices.index(vertix)] = 0
            for n in neighbours:
                row[vertices.index(n)] = 1
            graph_list.append(row)
        return graph_list

    @cached_property
    def distance_between_nodes(self):
        # shortest path from each node to others
        # https://favtutor.com/blogs/floyd-warshall-algorithm
        graph_list = self.graph_list()
        dist = list(map(lambda p: list(map(lambda q: q, p)), graph_list))
        num_vertices = len(graph_list)

        # Adding vertices individually
        for r in range(num_vertices):
            for p in range(num_vertices):
                for q in range(num_vertices):
                    dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
        return dist

    def total_flow_rate(self, open):
        sum = 0
        for valve in open:
            sum += self.flow.get(valve, 0)
        return sum

    def depth_first(self, current, time_left, total, opened):
        current_total = total + self.total_flow_rate(opened) * (30 - time_left)
        for valve in self.valves_with_non_zero_flow_rate:
            if valve in opened:
                continue

            time_to_next = 1 + self.distance_between_nodes[self.all_valves.index(current)][self.all_valves.index(valve)]

            if (time_left + time_to_next) >= 30:
                continue

            new_total = total + time_to_next * self.total_flow_rate(opened)

            opened.append(valve)

            maximum_from_this_vertix = self.depth_first(valve, time_left + time_to_next, new_total, opened)

            if maximum_from_this_vertix > current_total:
                current_total = maximum_from_this_vertix
            opened.pop(-1)

        return current_total


def test():
    example = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB\n' \
              'Valve BB has flow rate=13; tunnels lead to valves CC, AA\n' \
              'Valve CC has flow rate=2; tunnels lead to valves DD, BB\n' \
              'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE\n' \
              'Valve EE has flow rate=3; tunnels lead to valves FF, DD\n' \
              'Valve FF has flow rate=0; tunnels lead to valves EE, GG\n' \
              'Valve GG has flow rate=0; tunnels lead to valves FF, HH\n' \
              'Valve HH has flow rate=22; tunnel leads to valve GG\n' \
              'Valve II has flow rate=0; tunnels lead to valves AA, JJ\n' \
              'Valve JJ has flow rate=21; tunnel leads to valve II'

    valve_shit = ValveShit(example)

    max_flow = valve_shit.depth_first('AA', 0, 0, [])

    assert max_flow == 1651, "\U0001F62E\U0001F62E"

    print('Test PT1 OK')

if __name__ == '__main__':
    test()

    task_input = Input('input.txt').read_task_input()
    valve_shit = ValveShit(task_input)

    max_flow = valve_shit.depth_first('AA', 0, 0, [])

    print(f'Part 1: maximum flow that can be released in 30 minutes is {max_flow}')
