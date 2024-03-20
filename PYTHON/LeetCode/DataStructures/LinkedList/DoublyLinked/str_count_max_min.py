'''
******************* PROBLEM STATEMENT
LC # 432
#LinkedIn

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY: O(1) All except Delete O(NlogN)
SPACE COMPLEXITY: O(1)

******** SOLUTION

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(N)

https://leetcode.com/problems/all-oone-data-structure/discuss/91428/Python-solution-with-detailed-comments

NOTE:
    - Solution creates double linked nodes representing frequency counts rather than strings
    the benefit of this is that the value of the nodes is a set with strings of that frequency which can
    be edited in constant time
    - DLL plus Hashmap combination allows for keeping order in constant time while allowing
    for retrieval of min and max in constant time as well
    - DS
    1. hashmap {string: freq}
    2. hashmap {freq: DoublyLinkedList}
    3. doubly linkedlist w/ dummy head and tail. value is set of strs with freq

******************* TAGS
'''

from collections import defaultdict

class AllOne:

    def __init__(self):
        self.max = None
        self.min = None
        self.count = defaultdict(lambda: 0)
        

    def inc(self, key: str) -> None:
        self.count[key] = self.count[key] + 1
        if self.max is None or self.count[key] > self.max[1]:
            self.max = (key, self.count[key])
            
        

    def dec(self, key: str) -> None:
        self.count[key] = self.count[key] - 1
        if self.count[key] == 0:
            del self.count[key]
            
        # if deleted key was min need to find new min
        values = self.count.values()
        if key == self.min[0] and values:
            # tups = [ (val, key)  for val, key in self.count.values()] 
            sorted = sorted(values, key=lambda x: x[1])
            self.min = sorted[0]
        elif key == self.min[0] and not values:
            self.min = None

        # if deleted key was max need to find new max
        if key == self.max[0] and values:
            sorted = sorted(values, key=lambda x: x[1])
            self.max = sorted[-1]
        elif key == self.max[0] and not values:
            self.max = None
            
    
    def getMaxKey(self) -> str:
        if self.max:
            return self.max[0]
        return ""
        

    def getMinKey(self) -> str:
        if self.min:
            return self.min[0]
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()