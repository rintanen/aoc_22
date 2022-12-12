from InputBase import InputBase
import string

elevation = dict(zip(string.ascii_lowercase, range(1, 27)))

class Input(InputBase):
    def read_task_input(self):
        return [line for line in self.raw_input.split('\n')]


def find_good_neighbours(adjacent, row_edge, col_edge):
    adjacent = list(filter(lambda loc: loc[0] >= 0 and loc[1] >= 0 and loc[0] < row_edge and loc[1] < col_edge,
                      adjacent))
    return adjacent


def get_neighbours(map, loc):
    adjacent = [(loc[0] - 1, loc[1]), (loc[0], loc[1] + 1), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1)]
    adjacent = find_good_neighbours(adjacent, len(map), len(map[0]))
    for adj in adjacent:
        if (elevation.get(map[adj[0]][adj[1]],
               elevation['a'] if map[adj[0]][adj[1]] == 'S' else elevation['z']) -
               elevation.get(map[loc[0]][loc[1]],
               elevation['a'] if map[loc[0]][loc[1]] == 'S' else elevation['z'])) > 1:
            adjacent.pop(adjacent.index(adj))
    return adjacent


def find_path_bfs(map, loc, dest):
    # https://en.wikipedia.org/wiki/Breadth-first_search
    explored = []
    queue = [[loc]]
    if loc == dest:
        return loc
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = get_neighbours(map, node)
            neighbours = [n for n in neighbours if n not in path]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == dest:
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
    loc, dest = find_location_and_destination(map)
    path = find_path_bfs(map, loc, dest)
    assert len(path) - 1 == 31
    print(f'Test OK\nrequired steps: {len(path) - 1}')


if __name__ == '__main__':
    test()
    map = Input('input.txt').read_task_input()
    loc, dest = find_location_and_destination(map)
    path = find_path_bfs(map, loc, dest)
    print(f'Part1\nrequired steps: {len(path) - 1}')
