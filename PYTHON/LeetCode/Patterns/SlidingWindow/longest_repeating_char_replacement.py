# ******************* PROBLEM STATEMENT
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# ******************* NOTES

# ******************* SOLUTION
# maxCount may be invalid at some points, but this doesn't matter, because it was valid earlier in the string, and all that matters is finding the max window that occurred anywhere in the string. Additionally, it will expand if and only if enough repeating characters appear in the window to make it expand. So whenever it expands, it's a valid expansion.
class Solution:
    @staticmethod
    def characterReplacement(s: str, k: int) -> int:
        alpha = [0] * 26
        left, right = 0, 0
        max_count = 0

        for index, char in enumerate(s):
            alpha[ord(char)-ord('A')] += 1
            max_count = max(max_count, alpha[ord(char)-ord('A')])

            if max_count + k < right - left + 1: # need to shift left cuz not possible to fill left to right w/ 1 char after flipping k
                alpha[ord(s[left])] -= 1
                left += 1

                # NOW max_count may not longert make sense to use in if statement

        return max_count + k


# NOTE: Basing on preceeding character doesnt work. would only look at one char (whichever char is first). need to consider
# flipping any char

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = 0
#         max_count = 0
#
#         flip_index = []
#         repeating_char = None # TODO
#
#         for index, char in enumerate(s):
#             if repeating_char:
#                 if char == repeating_char:
#                     count += 1
#                 else: # non-repeating char
#                     if len(flip_index) < k: # flip
#                         flip_index.push(index)
#                         count += 1
#                     else: # update pointers
#
#             else: # first char
#                 repeating_char = char
#                 count += 1
#
#             max_count = max(max_count, count)





