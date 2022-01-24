'''
******************* PROBLEM STATEMENT
LC # ___

******************* NOTES
    - Not passing all test cases
******** MY IMPLEMENTATION:

TIME COMPLEXITY: O nlogn
SPACE COMPLEXITY: O n

******** SOLUTION
https://leetcode.com/problems/number-of-orders-in-the-backlog/discuss/1119992/JavaC%2B%2BPython-Priority-Queue
    - Very clean solution
    - Eliminates redundant code
    - Takes advantage of the fact that buy and sell scenarios can be treated identically with one while loop
    Solves the problem in half the number of lines of code

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''
import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell = [] #dec
        buy = [] # inc
        
        # execute orders
        for order in orders:
            print(f'iter: buy {buy} sell {sell}')
            p, a, type = order
            if type == 0: # buy
                while sell and sell[0][0] <= p and a >= 0:
                    print(f'IN BUY: buy {buy} sell {sell}')
                    # can buy from lowest price
                    if a >= sell[0][1]:
                        a = a - sell[0][1]
                        sell.pop(0)
                        continue
                    else:
                        sell[0][1] = sell[0][1] - a
                        a = 0
                        break
                if a > 0:
                    heapq.heappush(buy, [-p, a]) # I think i will need to add an index to preserve order
            elif type == 1: # sell
                while buy and -buy[0][0] >= p and a >= 0:
                    # can sell to highest price
                    if a >= buy[0][1]:
                        a = a - -buy[0][1]
                        buy.pop(0)
                        continue
                    else:
                        buy[0][1] = buy[0][1] - a
                        a = 0
                        break
                if a > 0:
                    heapq.heappush(sell, [p, a])
            # compute total backlog
        total_amount = 0
        for s in sell:
            total_amount += s[1]
        for b in buy:
            total_amount += b[1]
        return total_amount % (10**9 + 7)

sol = Solution()
print(sol.getNumberOfBacklogOrders([[26,7,0],[16,1,1],[14,20,0],[23,15,1],[24,26,0],[19,4,1],[1,1,0]]))                
                
                    
                
        