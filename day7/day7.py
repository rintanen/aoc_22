from InputBase import InputBase

class Input(InputBase):
    def read_task_input(self):
        return self.raw_input.split('$ cd /\n')[1]


def set_in_dict(target_dict, nested_keys, new_value):
    first, rest = nested_keys[0], nested_keys[1:]
    if rest:
        try:
            if not isinstance(target_dict[first], dict):
                # if the key is not a dict, then make it a dict
                target_dict[first] = {}
        except KeyError:
            # if key doesn't exist, create one
            target_dict[first] = {}

        set_in_dict(target_dict[first], rest, new_value)
    else:
        target_dict[first] = new_value


def create_file_tree(command_segments, base_dir):
    tree = {base_dir: {}}
    path = [base_dir]
    for command_segment in command_segments:
        command = command_segment[0]
        if command == 'ls':
            files = [file.split() for file in command_segment[1:]]
            new_dir = {name: {} if size_or_dir == 'dir' else int(size_or_dir)
                       for size_or_dir, name in files}
            set_in_dict(tree, path, new_dir)
        if command.startswith('cd'):
            next_dir = command.split()[1]
            if next_dir == '..':
                path.pop(-1)
            else:
                path.append(next_dir)
    return tree


def dict_values(d, depth):
    if depth == 1:
        for i in d.values():
            yield i
    else:
        for v in d.values():
            if isinstance(v, dict):
                for i in dict_values(v, depth-1):
                    yield i


def dict_depth(d):
    depth = 0
    for i in str(d):
        if i == "{":
            depth += 1
    return depth


def folder_size(folder):
    current_sum = 0
    for key in folder:
        if not isinstance(folder[key], dict):
            if not isinstance(folder[key], str):
                current_sum = current_sum + folder[key]
        else:
            current_sum = current_sum + folder_size(folder[key])
    return current_sum


if __name__ == '__main__':
    command_segments = Input('input.txt').read_task_input().split('$')[1:]
    command_segments = [segment.split('\n') for segment in command_segments]
    command_segments = [[s.lstrip() for s in segment if s != ''] for segment in command_segments]
    base = '/'
    tree = create_file_tree(command_segments, base_dir=base)

    all_folder_sizes = []
    for level in range(1, dict_depth(tree)+1):
        db = 1
        for dir in dict_values(tree, level):
            if isinstance(dir, dict):
                all_folder_sizes.append(folder_size(dir))

    under_100000 = [f for f in all_folder_sizes if f <= 100000]
    print(f'PART 1: {sum(under_100000)}')  # 1555642

    total_disk_space = 70000000
    required_unused_disk_space = 30000000
    remaining_disk_space = 70000000 - max(all_folder_sizes)
    big_enough = [f for f in all_folder_sizes if f >= (required_unused_disk_space - remaining_disk_space)]
    print(f'PART 2: {min(big_enough)}')  # 5974547





