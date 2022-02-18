from typing import List
from collections import defaultdict

'''
n = number of strings
m = largest string
Approach 1:


    time: n**2*(mlog(m))
    space: n

Approach 2:
    time: O(n*m)
    space: O(n*m)



'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(lambda: [])
        for string in strs:
            alpha_numeric = [0] * 26
            
            for char in string:
                alpha_numeric[ord(char) - ord('a')] += 1 # NOTE: Py: Method Unicode codes dont start from one
            
            anagram_dict[tuple(alpha_numeric)].append(string) # NOTE: Py: Method You can convert a list to a tuple using tuple(list). Remember that key needs to be immutable hence why it has to be tuple
        
        return [lst for lst in anagram_dict.values()] # NOTE: Py: Method Can just return values as they are arrays and values returns an array of them
                
                
            
    
    # def groupAnagramsApproach1(self, strs: List[str]) -> List[List[str]]:
    #     anagrams = []
    #     alphabetized = []
    #     for string in strs:
    #         ordered_string = sorted(string) # NOTE: 
    #         found = False
    #         for index, ordered in enumerate(alphabetized):
    #             if ordered_string == ordered:
    #                 anagrams[index].append(string)
    #                 found = True
    #                 break
    #         if not found:
    #             anagrams.append([string])
    #             alphabetized.append(ordered_string)
    #     return anagrams
            
                    

          
        # tuple_dict = defaultdict(list)
        # for string in strs:
        #     chars = [0] * 26
        #     for char in string:
        #         chars[ord(char) - ord('a')] += 1
        #     tuple_dict[tuple(chars)].append(string)
        # return tuple_dict.values()
        