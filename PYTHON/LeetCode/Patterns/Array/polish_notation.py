from collections import deque
from typing import List
import math

'''
    Remember:
        Order matters in how operations are applied i.e. -, /
        It says to round towards 0 in division
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set() # NOTE: Python Syntax operands = set({'+', '-', '*', '/'}) also works.
        operands.update(['+', '-', '*', '/']) # NOTE: Python Syntax. Add multiple items to a list

        stack = deque()

        for token in tokens:
            if token in operands:
                first = stack.pop() # NOTE: Tokens is a list of str
                second = stack.pop()

                if token == '+':
                    stack.append(second+first)
                elif token == '-':
                    stack.append(second-first)
                elif token == '*':
                    stack.append(second*first)
                else:
                    result = second/first # NOTE: That trimming the decimal w. int is equivalent to rounding towards 0
                    if result > 0:
                        stack.append(math.floor(result))
                    else:
                        stack.append(math.ceil(result))
                    
                print(f"{second}{token}{first}")
            else:
                stack.append(int(token))
                print(f"{token}")
        return stack.pop()