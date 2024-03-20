'''
******************* PROBLEM STATEMENT
LC # 1801

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY: nlogn
SPACE COMPLEXITY: n

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''

from collections import deque, heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []

        for p, a, type in orders:
            if type == 0: # BUY
                heapq.heappush(buy, [-p, a])
            else: # SELL
                heapq.heappush(sell, [p, a])

            while buy and sell and -buy[0][0] >= sell[0][0]:
                amount = min(buy[0][1], sell[0][1])

                if buy[0][1] == amount:
                    heapq.heappop(buy)
                else:
                    buy[0][1] = buy[0][1] - amount
                
                if sell[0][1] == amount:
                    heapq.heappop(sell)
                else:
                    sell[0][1] = sell[0][1] - amount
        
        total_amount = 0
        for _, amount in buy + sell:
            total_amount += amount
        return total_amount % (10**9 + 7) # NOTE: Remember modulo part. Remember to put modulo part in paranthesis

