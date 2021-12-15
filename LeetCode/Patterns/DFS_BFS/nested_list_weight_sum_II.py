'''
    LC # 364
    
    NOTE:
        - Immutable vars, like string or int, need to be modified in scope if they are being modified in a nested fxn (see max_d in this case)
        
    - Time Complexity: O(n) where n is number of numbers
    - Space Complexity: O(n) can be reduced to O(1) by running two iterations. first one just calculates max depth
    
    - This solution is most similar to approach #1 except it does one pass
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from typing import List


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # calculate the depth 
        # calculate max depth
        
        if not nestedList:
            raise Exception("Empty List")
        
        max_d = 0 # NOTE: max_d is not actually modified in this scope
        d = 0
        depth_num = [] # (depth, num)
        
        max_d = self.recurseList(nestedList, depth_num, d, max_d)
        
        sum = 0
        
        for tup in depth_num:
            weight = (max_d - tup[0] + 1)
            sum += tup[1] * weight
        
        return sum
        

                
                
    def recurseList(self, nestedList: List[NestedInteger], depth_num: int, d: int, max_d: int):
            d += 1
            for x in nestedList:
                max_d = max(max_d, d)
                if x.isInteger():
                    depth_num.append( (d, x.getInteger()) )
                else:
                    max_d = max(self.recurseList(x.getList(), depth_num, d, max_d), max_d) # NOTE: Need getList bc x is of type NestedInteger
            return max_d # NOTE: max_d needs to be modified in this scope