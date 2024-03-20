import sys
from typing import List
# ******************* PROBLEM STATEMENT

# ******************* NOTES
# Time Complexity = O(2N) -> O(N) because you can visit each num at most twice


# ******************* SOLUTION

class Solution:
    @staticmethod
    def minSubArrayLen(target: int, nums: List[int]) -> int:
        ans, length, sum, left, right = 0, 0, 0, 0, 0 # NOTE: Dont need length, length = right - left + 1
        min_length = sys.maxsize # TODO: Verify

        while right < len(nums):
            sum += nums[right]
            length += 1

            if sum >= target:
                while sum >= target: # NOTE: answer wont change if left stays put
                    if sum >= target:
                        if length < min_length:
                            ans = length
                            min_length = length
                    sum -= nums[left]
                    left += 1
                    length -= 1

            right += 1
        return ans


if __name__ == '__main__':
    assert Solution.minSubArrayLen(4, [1,4,4]) == 1
    assert Solution.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert Solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0