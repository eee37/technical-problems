'''
    Smart DFS solution:
        https://leetcode.com/problems/concatenated-words/discuss/159348/Python-DFS-readable-solution
'''
from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        alpha = defaultdict(lambda: [])
        
        curr_pointers = []
        concat_words = []
        
        # create alpha dict
        for word in words:
            curr = Node(word[0])
            alpha[word[0]].append(curr)
            if len(word) > 1:
                for char in word[1:]:
                    curr.next = Node(char)
                    curr = curr.next
            
        
        # check for concatenations
        for word in words:
            concat_count = 0
            for index,char in enumerate(word):
                nxt_pointers = []
                # validate nodes for next step
                for index,node in enumerate(curr_pointers):
                    if node is None:
                        if index < len(word)-1:
                            concat_count += 1
                    elif node.val == char:
                        nxt_pointers.append(node)   
                # add new nodes and assign next
                curr_pointers = []
                for node in nxt_pointers + alpha[char]:
                    curr_pointers.append(node.next)
            if concat_count > 1:
                concat_words.append(word)

        return concat_words