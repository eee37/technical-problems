'''
******************* PROBLEM STATEMENT
LC # 187

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION
n = length of string

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1) if you dont include response

******************* TAGS
#String #Set
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ten_letter_sequences = set()
        start = 0
        end = 9
        result = set() # NOTE: Use set to prevent duplicates
        
        while end < len(s):
            if s[start:end+1] in ten_letter_sequences:
                result.add(s[start:end+1])
            else:
                ten_letter_sequences.add(s[start:end+1])
            start += 1
            end += 1
        
        return list(result)