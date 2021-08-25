# The example function below keeps track of
# the opponent's history and plays whatever
# the opponent played two plays ago.
# It is not a very good player so you will
# need to change the code to pass the challenge.
import keras
import tensorflow as tf
import numpy as np
import time
import itertools

n_tot = 0
def player(prev_play, output=[], matrix=[{}]):
    # First State/Instance
    global n_tot
    hand = ['R', 'P', 'S']
    attack = {'R': 'P', 'P': 'S', 'S': 'R'}
    decay = .9 # machine 'forgetting' over time

    # CREATE KEYS/MATRIX
    keys = []
    for i in itertools.product(hand, hand, hand, hand):
        keys.append("".join(i))
    n_tot += 1
    # Initial Case
    if prev_play == '':
        prev_play = np.random.choice(hand)
        for i in keys:
            matrix[0][i] = 0
    if n_tot == 1000:
        for i in keys:
            matrix[0][i] = 0
        n_tot = 0
    if n_tot == 501:
        for i in keys:
            matrix[0][i] = 0

    output.append(prev_play)
    predict = output[-1]
    last_three = "".join(output[-4:])
    # Future Cases
    if len(last_three) == 4:
        matrix[0][last_three] += 1

        potential_plays = [
            last_three[-3:] + 'R',
            last_three[-3:] + 'P',
            last_three[-3:] + 'S',
        ]
        prob_matrix = {
            k: matrix[0][k] for k in potential_plays if k in matrix[0]
        }
        predict = max(prob_matrix, key=prob_matrix.get)[-1:]

    return attack[predict]

# def player(prev_play, opponent_history=[], pair_predict=[], output=[]):
#     # First State/Instance
#     hand = ['R', 'P', 'S']
#     attack = {'R': 'P', 'P': 'S', 'S': 'R'}
#     decay = .9 # machine 'forgetting' over time
#     if prev_play == '':
#         output.append(np.random.choice(hand))
#         pair_update = ''
#         pair_predict.append('')
#         opponent_history.append(prev_play)
#     else:
#         pair_update = pair_predict[-1]
#         pair_predict.append(''.join(output[-1:])+prev_play)
#         opponent_history.append(prev_play)
#         if pair_update != '':
#             # CREATE HOW FAR U WANT TO LOOK BACK
#             keys = []
#             for i in itertools.product(hand, hand):
#                 keys.append("".join(i))
#             # CREATE MATRIX
#             matrix = {}
#             for i in keys:
#                 matrix[i] = {'R': {'prob': 1 / 3,
#                                         'n_played': 0},
#                                   'P': {'prob': 1 / 3,
#                                         'n_played': 0},
#                                   'S': {'prob': 1 / 3,
#                                         'n_played': 0}}
#             # UPDATE FOR GIVEN INPUT (THIS SECTION CAN SWITCH pair_predict[-1] for pair_update and opponent_history[-1] for prev_play)
#             for i in matrix[pair_predict[-1]]:
#                 matrix[pair_predict[-1]][i]['n_played'] *= decay
#             matrix[pair_predict[-1]][prev_play]['n_played'] += 1
#             n_total = 0
#             for i in matrix[pair_predict[-1]]:
#                 n_total += matrix[pair_predict[-1]][i]['n_played']
#
#             for i in matrix[pair_predict[-1]]:
#                 matrix[pair_predict[-1]][i]['prob'] = matrix[pair_predict[-1]][i]['n_played'] / n_total
#
#             # for i in matrix[pair_update]:
#             #     matrix[pair_update][i]['n_played'] *= decay
#             # matrix[pair_update][opponent_history[-2]]['n_played'] += 1
#             # n_total = 0
#             # for i in matrix[pair_update]:
#             #     n_total += matrix[pair_update][i]['n_played']
#             #
#             # for i in matrix[pair_update]:
#             #     matrix[pair_update][i]['prob'] = matrix[pair_update][i]['n_played'] / n_total
#
#             # PREDICT OUTPUT
#             prob_matrix = matrix[pair_predict[-1]]
#             if max([v['prob'] for k,v in prob_matrix.items()]) == \
#                     min([v['prob'] for k,v in prob_matrix.items()]):
#                 output.append(np.random.choice(hand))
#             else:
#                 # print([v['prob'] for k,v in prob_matrix.items()])
#                 output.append(max([(v['prob'], k) for k,v in prob_matrix.items()])[1])
#                 # print(output[-1])
#         else:
#             output.append(np.random.choice(hand))
#
#     return attack[output[-1]]
#
#
