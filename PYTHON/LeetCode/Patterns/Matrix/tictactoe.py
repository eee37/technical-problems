from typing import List
'''
    NOTE:
        1. Tuples are immutable
'''

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Ways to win
        ways = []

        ways.append(lambda arr: arr[0] == 0)
        ways.append(lambda arr: arr[0] == 1)
        ways.append(lambda arr: arr[0] == 2)
        ways.append(lambda arr: arr[1] == 0)
        ways.append(lambda arr: arr[1] == 1)
        ways.append(lambda arr: arr[1] == 2)
        ways.append(lambda arr: arr[0] == arr[1])
        ways.append(lambda arr: arr[0] + arr[1] == 2)

        score_a = [0] * 8
        score_b = [0] * 8

        for index, move in enumerate(moves):
            # a's turn
            if index % 2 == 0:
                for score_index, way in enumerate(ways): # NOTE: Time complexity can be improved by instead checking index rather than trying out each method of winning -> Therefore, a player will win if the value of any line equals n or -n. Thus after a move [row, col], we could calculate the value of row row and column col and check if the absolute value equals n. If this move is placed on the diagonal or the anti-diagonal, then we will check if the absolute value of the relative value equals n as well.
                    if way(move):
                        score_a[score_index] += 1
                        if score_a[score_index] == 3:
                            return 'A'
            # b's turn
            else:
                for score_index, way in enumerate(ways):
                    if way(move):
                        score_b[score_index] += 1
                        if score_b[score_index] == 3:
                            return 'B'

        if len(moves) == 9:
            return 'Draw'

        return 'Pending'