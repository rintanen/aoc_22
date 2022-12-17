from InputBase import InputBase
from functools import cached_property
import numpy as np
from parse import parse


class Input(InputBase):
    def read_task_input(self):
        valve_map = {}
        for line in self.raw_input.split('\n')
            split_strs = (' to valves ', ' tunnels lead') if 'valves' in line else (' to valve ', ' tunnel leads')
            begin, neighbours = line.split(split_strs[0])
            valve, flow_rate = parse("Valve {} has flow rate={:d};" + split_strs[1], begin)
            valve_map[valve] = {'flow_rate': flow_rate, 'neighbours': neighbours.split(', ')}
        return valve_map


def find_neighbour_with_biggest_flow_rate(map, neighbours):
    compare_to = 0
    biggeest = []
    for nb in neighbours:
        if map[np]['flow_rate'] >= compare_to:
            biggeest.append(nb)
    db = 1


def find_next_valve(map, current_valve, opened):
    db = 1
    unopened_neighbours = [nb for nb in map[current_valve]['neighbours'] if not nb in opened]






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

    map = {}
    for line in example.split('\n'):
        split_strs = (' to valves ', ' tunnels lead') if 'valves' in line else (' to valve ', ' tunnel leads')
        begin, neighbours = line.split(split_strs[0])
        valve, flow_rate = parse("Valve {} has flow rate={:d};" + split_strs[1], begin)
        map[valve] = {'flow_rate': flow_rate, 'neighbours': neighbours.split(', ')}
    db = 1

    minutes = 30
    opened = []
    pressure_relieved = 0
    current_valve = list(map.keys())[0]
    for _ in range(minutes):
        pressure_relieved += map[current_valve]['flow_rate'] if current_valve not in opened else 0
        opened.append(current_valve)
        find_next_valve(map, current_valve, opened)



    # Algoritmi
    # 1. Tarkista onko naapureissa joku valve kiinni, jos on niin mene sinne joka vapauttaa eniten painetta
    # jos ei ole niin tarkista onko naapureiden naapureissa joku jossa on venttiili kiinni
    # Jos 2 valvea vapauttaa yhtä paljon painetta ota se kumman seuraava naapuri vapauttaa enemmän jne.
    # toimii koska jokaisen noden välillä on yhtä pitkä matka

if __name__ == '__main__':
    test()