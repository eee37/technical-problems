import math
import re
'''
    Learnings:
        1. Remember about 0 index and how it affects loops and indexing
        2. Instead should use pointers location to determine when to stop
            so stop when pointers are equal
        
        
    TODO: Return to this problem solution is locked!!!
    
    
    TIME, SPACE
'''

class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '',  s.replace(' ', '').lower())
        end = len(s)

        for i in range(math.floor(end - 1 / 2)): # Not sure why the -1 needs to be placed here
            if s[i] == s[end - i - 1]: # -1 bc of 0 index
                continue
            else:
                return False

        return True


if __name__ == '__main__':
    print(Solution.isPalindrome('aba'))
    print(Solution.isPalindrome('abba'))
    print(Solution.isPalindrome(''))
    print(Solution.isPalindrome('a'))
    print(Solution.isPalindrome('a a'))
    print(Solution.isPalindrome('ab')) # False
    print(Solution.isPalindrome('A man, a plan, a canal: Panama'))  # True
