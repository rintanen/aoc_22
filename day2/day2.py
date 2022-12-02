from InputBase import InputBase


class Input(InputBase):
    def read_task_input(self):
        pass


WIN_CHART = {'X': 'C',
             'Y': 'A',
             'Z': 'B'}


LOSE_CHART = {'X': 'B',
              'Y': 'C',
              'Z': 'A'}

WIN_CHART_PT2 = {'A': 'B',
                 'B': 'C',
                 'C': 'A'}

LOSE_CHART_PT2 = {'A': 'C',
                  'B': 'A',
                  'C': 'B'}


def outcome(opponent_plays, i_play):
    """ 6 for win, 3 for draw, 0 for lose """
    points = 3
    if WIN_CHART[i_play] == opponent_plays:
        points = 6
    elif LOSE_CHART[i_play] == opponent_plays:
        points = 0
    return points


if __name__ == '__main__':
    task_input = Input('input.txt')

    extra_points = {'X': 1,
                    'Y': 2,
                    'Z': 3,
                    'A': 1,
                    'B': 2,
                    'C': 3}

    score_pt1 = 0
    score_pt2 = 0
    for item in task_input.raw_input:
        # PT1
        opponent_plays, i_play = item.strip().split(' ')
        score_pt1 += outcome(opponent_plays, i_play) + extra_points[i_play]

        # PT2
        if i_play == 'X':  # lose
            i_play = LOSE_CHART_PT2[opponent_plays]
        elif i_play == 'Y':  # draw
            i_play = opponent_plays
            score_pt2 += 3
        elif i_play == 'Z':  # win
            i_play = WIN_CHART_PT2[opponent_plays]
            score_pt2 += 6

        score_pt2 += extra_points[i_play]

    print(f'part 1: {score_pt1}')
    print(f'part 2: {score_pt2}')


