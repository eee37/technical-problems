'''
******************* PROBLEM STATEMENT
LC # 526
#LinkedIn
******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY: O(N!)
SPACE COMPLEXITY: O(N)

******** SOLUTION

TIME COMPLEXITY: 
SPACE COMPLEXITY:

******************* TAGS
'''

class Solution:
    def __init__(self):
        self.count = 0
    def countArrangement(self, n: int) -> int:

        def count(i, num_set):
            if i == 1: # NOTE: Can stop at 1 bc all numbers are divisible by 1
                self.count += 1 # NOTE: Syntax can't just return total bc it will end all execution
            for j in num_set:
                if i % j == 0 or j % i == 0:
                    count(i-1, num_set - {j})

        count(n, set(range(1, n+1))) # NOTE: An iterator fed to a set initalizer creates a set

        return self.count

sol = Solution()
sol.countArrangement(2)