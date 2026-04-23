"""
    NOTE:
    - Can do a monostack loopping forward.
    - there is a faster solution that also processes the temps backwards but takes advantage of the information contained in ans to jump to hotter indices. This turns out to be much faster in some scenarios + more space efficient
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        ans = [0] * len(temperatures)

        for index in range(len(temperatures)-1, -1,-1):
            while len(stack) > 0:
                if stack[-1][0] > temperatures[index]:
                    ans[index] = stack[-1][1] - index
                    break
                else:
                    stack.pop()
            if len(stack) == 0: # optional
                ans[index] = 0
            stack.append((temperatures[index], index))
        return ans



"""
ans 1 , 2, 1, 0
55, 1
60, 3

[30,55,50,60]

0: 3,60 -> 0  stack []
1: 2,50 ->  1            stack (60, 3) 
2: 1, 55 -> 2                stack (50, 2: 60, 3) -> stack (: 60, 3)
"""