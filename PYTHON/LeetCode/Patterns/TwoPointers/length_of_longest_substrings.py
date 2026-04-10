"""
    #3
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
    Took me 25 min to come up with first answer. First answer was correct

    TIME: O(n)
    SPACE: O(n) -> The upper bound is based on the size of the character set as that is the longest string possible. This would be O(1) as its a connstant
    
    SOLUTION:
    Space complexity : O(min(m,n)). Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.

    There is a more optimal solution that uses a map instead to get the index where the current seen character was seen
    """
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    seen = set()
    longest = 0
    left = 0

    for right in range(len(s)):
        if s[right] not in seen:
            longest = max(longest, right-left + 1)
            seen.add(s[right])
        else:
            while s[left] != s[right] and left < right:
                seen.remove(s[left])
                left += 1
            left += 1
    return longest


assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3



        