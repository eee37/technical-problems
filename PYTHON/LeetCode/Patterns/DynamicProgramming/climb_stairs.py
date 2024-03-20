# use default dict
from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = defaultdict(lambda:False)
        cache.update({1: 1})
        cache.update({2: 2})
        if n <=0:
            return 0
        return self.recurse(n, cache)

    def recurse(self, n, cache):
        if cache.get(n):
            return cache.get(n)
        return self.recurse(n-1, cache) + self.recurse(n-2, cache)

# use default dict
'''
    Time: O(n)
    Space: O(n)
    NOTE: 
    1. Need to realize that DP[n] =  D[n-1] + D[n-2]. Looking at binary tree helps with this
    2. To convert from recursive algo with space complexity to iteritive solution need to tackle down-top approach
'''
from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = defaultdict(lambda: False)
        cache.update({1: 1})  # Note: could use array. [0] * n+1
        cache.update({2: 2})
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return cache.get(n)
        for num in range(3, n + 1):  # Note: the need to use +1 cause range stops at before upper bound [)
            sum = cache.get(num - 1) + cache.get(num - 2)
            cache.update({num: sum})
        return cache.get(n)