from collections import Counter

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hashmap = Counter(s)

    for char in t:
        if char not in hashmap:
            return False
        hashmap[char] -= 1
    
    for value in hashmap.values():
        if value < 0 or value > 0:
            return False
    return True

assert isAnagram('anagram', 'nagaram') == True
assert isAnagram('rat', 'car') == False