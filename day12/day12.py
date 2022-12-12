from InputBase import InputBase
import string
import math

elevation = dict(zip(string.ascii_lowercase, range(1, 27)))
elevation.update({'S': 1, 'E': 26})

class Input(InputBase):
    def read_task_input(self):
        return [line for line in self.raw_input.split('\n')]


def filter_adjacent(adjacent, row_edge, col_edge):
    adjacent = list(filter(lambda loc: loc[0] >= 0 and loc[1] >= 0 and loc[0] < row_edge and loc[1] < col_edge,
                      adjacent))
    return adjacent


def get_neighbours(map, loc, reverse):
    adjacent = [(loc[0] - 1, loc[1]), (loc[0], loc[1] + 1), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1)]
    adjacent = filter_adjacent(adjacent, len(map), len(map[0]))
    keep = []
    for i, adj in enumerate(adjacent):
        if not reverse:
            # PT 1 Check that adjacent step is not more than 1 step HIGHER
            if not elevation[map[adj[0]][adj[1]]] - elevation[map[loc[0]][loc[1]]] > 1:
                keep.append(adj)
        else:
            # PT 2 here we need to check that adjacent step is not more than 1 step LOWER
            if not elevation[map[loc[0]][loc[1]]] - elevation[map[adj[0]][adj[1]]] > 1:
                keep.append(adj)
    return keep


def find_path_bfs(map, loc, dest, reverse=False):
    # https://en.wikipedia.org/wiki/Breadth-first_search
    # https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
    explored = []
    queue = [[loc]]
    if loc == dest:
        return loc
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = get_neighbours(map, node, reverse)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if map[neighbour[0]][neighbour[1]] == dest:
                    return new_path
            explored.append(node)
    # didnt find a path
    return loc


def find_location_and_destination(map):
    loc = ()
    dest = ()
    for i, line in enumerate(map):
        if 'S' in line:
            loc = (i, (len(line) - len(line.split('S')[1])) - 1)
        if 'E' in line:
            dest = (i, (len(line) - len(line.split('E')[1])) - 1)
    return loc, dest


def test():
    map = 'Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi'
    map = [line for line in map.split('\n')]
    start_location, end_location = find_location_and_destination(map)
    path = find_path_bfs(map, start_location, 'E')
    assert len(path) - 1 == 31
    print(f'Test PT1 OK\nrequired steps: {len(path)-1}')
    path = find_path_bfs(map, end_location, 'a', reverse=True)
    assert len(path) - 1 == 29
    print(f'Test PT1 OK\nrequired steps: {len(path)-1}')


if __name__ == '__main__':
    test()
    map = Input('input.txt').read_task_input()

    # Find index of letters S and E
    S, E = find_location_and_destination(map)

    # Find the shortest path from "S" to E
    path = find_path_bfs(map, S, 'E')
    print(f'Part1\nrequired steps: {len(path) - 1}')

    # Find the shortest path from "S" to a (a is the lowest point in the map)
    path = find_path_bfs(map, E, 'a', reverse=True)
    print(f'Part2\nrequired steps: {len(path) - 1}')

