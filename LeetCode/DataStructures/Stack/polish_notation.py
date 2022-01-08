'''
******************* PROBLEM STATEMENT
LC # 150

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

- NOTE: Solution uses hashmap for more elegant solution
TIME COMPLEXITY: On
SPACE COMPLEXITY: On

******************* TAGS
#Stack
'''

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operands = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operands:
                one = int(stack.pop())
                two = int(stack.pop())
                if token == '+':
                    stack.append(two + one)
                elif token == '-':
                    stack.append(two - one)
                elif token == '*':
                    stack.append(two * one)
                else:
                    stack.append(two / one)
            else:
                stack.append(token)

        return int(stack.pop()) # TODO: What does always truncate to 0 mean
        