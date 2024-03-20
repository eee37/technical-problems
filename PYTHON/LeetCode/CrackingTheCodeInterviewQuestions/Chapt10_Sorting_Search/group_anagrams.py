# ******************* PROBLEM STATEMENT
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# ******************* NOTES
# Ord() -> converts char to int representation of unicode. Reverse of char
# collections.defaultdict(list) -> Used to creat a dict that provides default value of empty list when key not present. The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
# y += x -> used to increment var
# ******************* SOLUTION
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_dict = defaultdict(list)
        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - ord('a')] += 1
            tuple_dict[tuple(chars)].append(string)
        return tuple_dict.values()

