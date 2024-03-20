'''
******************* PROBLEM STATEMENT
LC #526
#LinkedIn
******************* NOTES
    - Need to somehow track all counts. Difficult in this case cause its not a DP problem. Passing a var doesnt work well either
    my solution is to use a class var that exists outside the scope of fxn. 
    Solution aggregates all the responses by calling sum on all the results
    - Approach 3 is the easiest to read
        - Use a list to keep track of what has been tried
        - Starting a position 1 try every possible number and mark the number as visited
        - For the ones that work move to the next position and try all numbers that arent mark as visited
        - Add to count once all positions have been visited and REMEMBER to unmark a position as visited after its been tried
    https://leetcode.com/problems/beautiful-arrangement/discuss/99738/Easy-Python-~230ms
    This python solution takes similar approach
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