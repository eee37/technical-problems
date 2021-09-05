# ******************* PROBLEM STATEMENT
#Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.


# ******************* NOTES
# 1. I assumed that s would only contain alphabetic chars. This assumption turned out to be false
# 2. Note while loop that shifts left pointer until distinct < k true. Having WHILE loop w/ invariant helps in these type of problems
# 3. Note default dict accepts lambda fxn. Go over lambda fxn in python

# ******************* SOLUTION
# Time Complexity: O(2n) -> O(n)

from collections import defaultdict

class Solution:
    @staticmethod
    def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
        alpha = defaultdict(lambda: 0)
        left, right, distinct, longest = 0, 0, 0, 0

        while right < len(s):
            if alpha[ord(s[right])] == 0:
                distinct += 1

            alpha[ord(s[right])] += 1

            # cases where left needs to shift
            if distinct > k:
                while distinct > k:
                    alpha[ord(s[left])] -= 1
                    if alpha[ord(s[left])] == 0:
                        distinct -= 1
                    left += 1

            # otherwise shift right
            longest = max(longest, right - left + 1)
            right += 1

        return longest
# class Solution:
#     @staticmethod
#     def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
#         alpha = [0] * 26
#         left, right, distinct, longest = 0, 0, 0, 0
#
#         while right < len(s):
#             if alpha[ord(s[right]) - ord('a')] == 0:
#                 distinct += 1
#
#             alpha[ord(s[right]) - ord('a')] += 1
#
#             # cases where left needs to shift
#             if distinct > k:
#                 while distinct > k:
#                     alpha[ord(s[left]) - ord('a')] -= 1
#                     if alpha[ord(s[left]) - ord('a')] == 0:
#                         distinct -= 1
#                     left += 1
#
#             # otherwise shift right
#             longest = max(longest, right - left + 1)
#             right += 1
#
#         return longest

if __name__ == '__main__':
    assert Solution.lengthOfLongestSubstringKDistinct('aa', 1) == 2
    assert Solution.lengthOfLongestSubstringKDistinct('eceba', 2) == 3



