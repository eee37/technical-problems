'''
    ******************* PROBLEM STATEMENT
    LC # 648
    Note: 
        Py method. Map function is helpful when dealing with operations on array
        https://www.geeksforgeeks.org/python-map-function/
        
        Py method: Reduce is used to reduce elements in a list by successfively condencing elements
        in the list to one
        https://www.geeksforgeeks.org/reduce-in-python/
        
        Solution:
            Essentially what I was trying to implement in my first solution is a Trie
            This is a build in data-structure that is essentially a tree where each node
            represents a char in a word
            see https://www.geeksforgeeks.org/trie-insert-and-search/
            Approach 1:
                use set to store prefixes
                scan each word checking if scanned portion is found in set. if so return prefix/scanned portion
                once finish scanning return word
                Complexity analysis is confusing:
                    Explanation for time complexity: 
                        @ywen1995 Disagree. To calculate hash value of the string, you definitely have to iterate over every character, which takes linear time. It's very brave to assume that Python precalculates hash values for every prefix of the string.
'''
import re
class Node:
    def __init__(self, val, word):
        self.val = val
        self.word = word
        self.next = None
        
class Solution:
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_map = defaultdict(lambda: [])
        
        self.populate_map(dictionary, word_map)
        
        words_in_sentence = sentence.split()
        
        new_sentence = []
        nodes = []
        for word in words_in_sentence:
            print(f'word: {word}')
            count = len(new_sentence)
            for index, char in enumerate(word):
                if len(new_sentence) > count:
                    break
                if index == 0:
                    nodes = word_map[word[0]]
                    if len(nodes) == 0:
                        new_sentence.append(word)
                        break
                nxt = []
                for node in nodes:
                    print(f'node: {node.val}')
                    if node.val == char:
                        if node.next is None:
                            new_sentence.append(node.word)
                            nxt = []
                            break
                        nxt.append(node.next)
                    nodes = nxt
                if len(nodes) == 0 and len(new_sentence) == count:
                    new_sentence.append(word)
                    break
        return ' '.join(new_sentence)
    
    
    
    
    def populate_map(self, dictionary: List[str], word_map) -> None:
        for word in dictionary:
            curr = Node(word[0], word)
            # add to map then create linked list
            word_map[word[0]].append(curr)
            for char in word[1:]:
                curr.next = Node(char, word)
                curr = curr.next                
                
    
    '''
    # Approach 2 Using Regex
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words_in_sentence = sentence.split()
        new_sentence = []
        for word in words_in_sentence:
            matches = []
            for dict_word in dictionary:
                if re.search(f'^{dict_word}', word) is not None:
                    matches.append(dict_word)
            if not matches:
                new_sentence.append(word)
                continue
            min_size = matches[0]
            for match in matches:
                if len(match) < len(min_size):
                    min_size = match
            new_sentence.append(min_size)
        return ' '.join(new_sentence)
    '''
                
        
                    