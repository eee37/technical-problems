'''
LC # 271

TAGS: #String
'''
from typing import List


class Solution:
    '''
        n = # words
        s = length of s
        time complexity: O(n*s) NOTE that a loop will never check for than s chars
        non-optimal runs into time limit exceeded
    '''
    def numMatchingSubseqTwo(self, s: str, words: List[str]) -> int:
        ans = 0
        
        for word in words:
            pointer_s = 0
            pointer_w = 0
            
            while pointer_w < len(word) and pointer_s < len(s):
                if s[pointer_s] == word[pointer_w]:
                    pointer_s += 1
                    pointer_w += 1
                else:
                    pointer_s += 1
            
            if pointer_w == len(word):
                ans += 1
                
        return ans
    
    
    '''
    NOTE:
        SOLUTION:
            Approach 2 keeps code clean and simple by
                1.) Keeping a copy of old matches and setting placeholder as an empty list
                2.) Using iter to keep pointer to next char
                https://www.geeksforgeeks.org/python-iter-method/
                https://www.geeksforgeeks.org/python-next-method/
                3.) Note that using iter or Trie or LinkedList is more optimal as it doesn't require you
                    to recreate the string
    '''
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        alpha = [[] for _ in range(26) ] # NOTE: Py Syntax [] *26 returns an empty array
        # process words
        for word in words:
            index = ord(word[0]) - ord('a')
            alpha[index].append(word)
        
        for char in s:
            char_index = ord(char) - ord('a')
            if not alpha[char_index]:
                continue
            matches = alpha[char_index]
            replacement = []
            for index in range(len(matches)):
                # match = matches.pop(index) # NOTE: Lesson Don't want to modify list while looping through it
                match = matches[index]
                if len(match) == 1:
                    ans += 1
                    continue
                if char == match[1]:
                    replacement.append(match[1:])
                nxt = ord(match[1]) - ord('a')
                alpha[nxt].append(match[1:])
            alpha[char_index] = replacement
        return ans
                    
            
            
        