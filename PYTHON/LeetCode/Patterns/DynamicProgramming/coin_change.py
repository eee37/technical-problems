from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = [(0,0)] #(curr_amount, steps)
        best_answer = -1

        if amount == 0: # Base case
            return 0

        while queue:
            step = queue.pop(0)
            for coin in coins:
                if step[0] + coin < amount:
                    queue.append((step[0] + coin, step[1]+1))
                elif step[0] + coin == amount:
                    if best_answer == -1 or step[1]+1 < best_answer:
                        best_answer = step[1]+1

        return best_answer



'''
    Official DP Solution calculates the solution calculates the solution at every amount from [0, amount], using previously calculated solutions to calculate new ones. Bottom Up approach makes most sense
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = [(0,0)] #(curr_amount, steps)

        visited = [False] * amount
        best_answer = -1

        if amount == 0: # Base case
            return 0

        while queue:
            step = queue.pop(0)
            for coin in coins:
                if step[0] + coin < amount and not visited[step[0] + coin -1]: # Note: bc we are doing BFS we are guaranteed to be visiting an amount in the least possible number of steps so we can skip this amount if its visited later
                    queue.append((step[0] + coin, step[1]+1))
                    visited[step[0] + coin -1] = True
                elif step[0] + coin == amount:
                    if best_answer == -1 or step[1]+1 < best_answer:
                        best_answer = step[1]+1

        return best_answer
