class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                seen.append(char)
            elif len(seen) == 0:
                return False
            elif (char == ')' and seen[-1] != '(') or (char == '}' and seen[-1] != '{') or (char == ']' and seen[-1] != '['):
                return False
            else:
                seen.pop()
        return True if len(seen) == 0 else False


        