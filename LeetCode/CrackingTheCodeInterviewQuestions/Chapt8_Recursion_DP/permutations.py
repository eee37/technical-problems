from typing import List
'''
    Time Complexity: n * n!
    Space Complexity: n * n!
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        return Solution.permutations([], nums, len(nums), [])

    @staticmethod
    def permutations(curr, rem, size, soln):
        if len(rem) == 1:
            soln.append(curr + rem) # NOTE: Append returns None
            return soln

        # try every remaining int in the next position and pass current with remaining ints
        for remainIndex in range(len(rem)):
            temp_curr = curr[:] # NOTE: temp = curr would mean they point to same address and thus chaging one var equates to changing two
            temp_curr.append(rem[remainIndex]) # NOTE: Append returns None
            Solution.permutations(temp_curr, rem[:remainIndex] + rem[remainIndex+1:], size, soln)

        return soln

if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([]))
    print(sol.permute([1]))
    print(sol.permute([0,1]))
    print(sol.permute([1,2,3]))