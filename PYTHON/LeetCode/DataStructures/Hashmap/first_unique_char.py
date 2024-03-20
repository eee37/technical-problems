'''
    LC #387:
        NOTE:
            LC Solutions takes advantage of counter class that comes with existing functionality to convert list to hashmap with frequency
'''
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = defaultdict(lambda: 0)

        for char in s:
            count = seen[char] + 1
            seen.update({char: count})

        for index, char in enumerate(s):
            if seen[char] == 1:
                return index

        return -1