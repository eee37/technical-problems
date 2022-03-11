from collections import defaultdict
from typing import List
'''
    n = length of sentences
    m = length of similar pairs
    u = unique strings in similar pairs

    Space  Grows as the number of unique strings in similar pairs grows
    Space: O(m) # 2u comes from set in dfs and size of stack
    Time: O(m + nm)

    consider replacing m with u

    NOTE:
        SOLUTION:
            * Pairs is always of length 2
            * The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
            * https://www.pythontutorial.net/python-basics/python-while-else/

'''

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        # process pairs
        similar_map = defaultdict(lambda: set())
        
        for pair in similarPairs:
            for string in pair:
                # similar_map.update({string: pair}) # NOTE: Dont want to overrid when word appears in more than one pair
                similar_map[string] = similar_map[string].union(set(pair)) # NOTE: Want to merge pair with existing set of pairs linked to string
        # check if similar
        for index in range(len(sentence1)):
            similar = self.dfs(sentence1[index], sentence2[index], similar_map, set())
            if not similar:
                return False
        return True
            
    
    def dfs(self, one, two, similar_map, visited):
        if one == two:
            return True
        visited.add(one)
        for word in similar_map[one]:
            if word not in visited and self.dfs(word, two, similar_map, visited):
                return True
        return False

sol = Solution()
print(sol.areSentencesSimilarTwo(["I","love","leetcode"],
["I","love","onepiece"], 
[["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]))