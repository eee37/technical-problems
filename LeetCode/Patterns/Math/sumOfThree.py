from typing import List

'''
    Q:
        1. Are we only considering postive integers?

'''

class Solution:
    @staticmethod
    def sumOfThree(num: int) -> List[int]:
        if num % 3 != 0:
            return []
        return [int(num/3 - 1) , int(num/3), int(num/3 + 1)]
        '''
        # This solution exceeds time limit
        pos = 0
        sum = 3
        while sum <= num:
            pos = pos + 1
            sum = sum + 3
            if sum == num:
                return [pos, pos+1, pos+2]
        return []
        '''

print(Solution.sumOfThree(33))
print(Solution.sumOfThree(4))