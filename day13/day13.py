from InputBase import InputBase


class Input(InputBase):
    def read_task_input(self):
        return [pair.split('\n') for pair in self.raw_input.split('\n\n')]


def compare_nested_list(left, right):
    match (left, right):
        case (int(left), int(right)):
            return left - right
        case(int(left), list(right)):
            return compare_nested_list([left], right)
        case(list(left), int(right)):
            return compare_nested_list(left, [right])
        case(list(left), list(right)):
            for _ in range(len(min([left, right], key=len))):
                comp = compare_nested_list(left.pop(0), right.pop(0))
                if comp == '->':
                    return compare_nested_list(left, right)
                if isinstance(comp, bool):
                    return comp
                elif isinstance(comp, int):
                    if comp < 0:
                        return True
                    elif comp > 0:
                        return False
            if not left and not right:
                return '->'
            if len(left) < len(right):
                return True
            if len(left) > len(right):
                return False


def sort_packets(packets):
    sorted_packets = []
    smallest = 0
    while len(sorted_packets) < len(packets):
        for packet in packets:
            if packets.index(packet) in sorted_packets:
                continue
            if smallest == packets.index(packet):
                continue
            if compare_nested_list(eval(packets[smallest]), eval(packet)):
                continue
            smallest = packets.index(packet)
        sorted_packets.append(smallest)
        not_in_sorted_packets = [p for p in packets if packets.index(p) not in sorted_packets]
        if not_in_sorted_packets:
            smallest = packets.index(not_in_sorted_packets[0])
    return [packets[i] for i in sorted_packets]


def test():
    example_input = '[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n' \
                    '[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n' \
                    '[1,[2,[3,[4,[5,6,0]]]],8,9]'
    example_input = [pair.split('\n') for pair in example_input.split('\n\n')]
    correct = []
    for i, pair in enumerate(example_input, start=1):
        if compare_nested_list(eval(pair[0]), eval(pair[1])):
            correct.append(i)
    assert sum(correct) == 13
    print(f'Test PT1 OK\nsum of indices in correct order {sum(correct)}')

    # create list of all packets
    # add divider packets
    packets = ['[[2]]', '[[6]]']
    # concatenate other packets
    for pair in example_input:
        packets.append(pair[0])
        packets.append(pair[1])

    # sort packets
    packets = sort_packets(packets)

    decoder_key = (packets.index('[[2]]') + 1) * (packets.index('[[6]]') + 1)
    assert decoder_key == 140
    print(f'Test PT2 OK\ndecoder key {decoder_key}')


if __name__ == '__main__':
    test()

    task_input = Input('input.txt').read_task_input()

    # PT 1
    correct = []
    for i, pair in enumerate(task_input, start=1):
        if compare_nested_list(eval(pair[0]), eval(pair[1])):
            correct.append(i)
    print(f'\nPT1: sum of indices in correct order is {sum(correct)}')

    # PT 2
    # create list of all packets
    # add divider packets
    packets = ['[[2]]', '[[6]]']
    # concatenate the other packets
    for pair in task_input:
        packets.append(pair[0])
        packets.append(pair[1])

    # sort packets
    packets = sort_packets(packets)
    decoder_key = (packets.index('[[2]]') + 1) * (packets.index('[[6]]') + 1)
    print(f'PT2: decoder key is {decoder_key}')
