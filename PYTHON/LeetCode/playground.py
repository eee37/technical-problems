from collections import defaultdict
'''
    NOTE: Do not code until soln is found on paper
'''

class DDLinkedNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        max_size = 0
        cur_size = 0
        seen = defaultdict(None) # pos
        for idx, char in enumerate(s):
            if seen.get(char) is not None: # NOTE: How to read from a ditc
                cur_size = idx - seen.get(char)
            else:
                cur_size += 1
            seen.update({char: idx})
            if cur_size > max_size:
                max_size = cur_size
        return max_size

print(Solution.lengthOfLongestSubstring('abba'))
# print(Solution.lengthOfLongestSubstring('bbbbb'))
# print(Solution.lengthOfLongestSubstring('pwwkew'))



