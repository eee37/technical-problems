'''
******************* PROBLEM STATEMENT

******************* NOTES
1. Don't need to store sell price info contained in max profit
2. Python max value = machine's max value = sys.maxsize

TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: 0

******************* SOLUTION
'''
import sys
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        buyPrice = sys.maxsize

        for index, price in enumerate(prices):
            if price < buyPrice:
                buyPrice = price
            else:
                if price - buyPrice > maxProfit:
                    maxProfit = price - buyPrice

        return maxProfit

if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 5
    assert sol.maxProfit([7,6,4,3,1]) == 0
