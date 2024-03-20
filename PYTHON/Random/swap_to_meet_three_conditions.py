'''
    LC #1737
    
    NOTE: 
    SOLUTION:
    
    https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032021/Python-Poor-Question-Statement
        - For conditions 1 & 2 sums num of one string that need to be swapped right to number that need to be swapped right at each letter of the alphabet and finds the minimum
        - For conditions 3 similarly determines number needed to swap at each letter of the alphabet
        
    https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032070/JavaC%2B%2BPython-Clean-Solution
        - Conditions 1 & 2 can be handled by scanning arrays char, char
            updating ith entry to include sum of all entries 0...i-1
            Having sum of total entries with sum of all entries allows you to calculate
            how many swaps need to happen
        
'''
from typing import List


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        a_alpha = [0] * 26
        b_alpha = [0] * 26
        
        
        a_min_max = self.process_string(a, a_alpha)
        b_min_max = self.process_string(b, b_alpha)
        
        ans = float('inf')
        # condition one
        ans = min(ans, self.make_one_strictly_less(a_alpha, b_alpha, a_min_max, b_min_max))
        # condition two
        ans = min(ans, self.make_one_strictly_less(b_alpha, a_alpha, b_min_max, a_min_max))
        # condition three
        a_most_frequent = max(a_alpha)
        b_most_frequent = max(b_alpha)
        ans = min(ans, len(a) - a_most_frequent + len(b) - b_most_frequent)
        
        return ans
        
    
    def make_one_strictly_less(self, one: List[int], two: List[int], one_min_max, two_min_max):
        ans = float('inf')
        # change one to be stricly less than two
        if two_min_max[0] > 0: # NOTE: This denotes ord('a') since we subtract ord('a')
            count = 0
            if one_min_max[1] >= two_min_max[0]: # NOTE: We might not need to convert any
                for freq in one[one_min_max[0]: two_min_max[1] + 1]: # NOTE: Range that need to be updated
                    count += freq
            ans = min(ans, count)
        # change two to be stricly greater than one
        elif one_min_max[1] < ord('z') - ord('a'):
            count = 0
            if one_min_max[1] >= two_min_max[0]: # NOTE: We might not need to convert any
                for freq in two[two_min_max[0]: one_min_max[1] + 1]:
                    count += freq
                ans = min(ans, count)
        return ans
        
    
    
    def process_string(self, string: str, alpha: List[int]):
        max_alpha_numeric = 0 # NOTE: This denotes ord('a') since we subtract ord('a')
        min_alpha_numeric = ord('z') - ord('a')
        for char in string:
            alpha_numeric = ord(char) - ord('a')
            alpha[alpha_numeric] += 1
            max_alpha_numeric = max(max_alpha_numeric, alpha_numeric)
            min_alpha_numeric = min(min_alpha_numeric, alpha_numeric)
        return (min_alpha_numeric, max_alpha_numeric)