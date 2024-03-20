'''
    Unresolved Issue: <class 'TypeError'>, TypeError("'Node' object is not callable"), <traceback object at 0x1029b6988> at the beginning of pop fxn being called

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top = None
        self.min = None

    class Node:
        def __init__(self, val: int, next=None, prev_min=None):
            self.val = val
            self.next = next
            self.prev_min = prev_min

    def push(self, val: int) -> None:
        self.top = MinStack.Node(val, self.top, self.min)
        # update min if neccessary
        if self.min:  # NOTE: Need to check for None here
            if val < self.min:
                self.min = val
        else: # NOTE: Need to handle case min is None
            self.min = val

    def pop(self) -> None:
        if self.top:
            # update min if neccessary
            if self.min == self.top.val:  # if there are more than one nodes w/ same min this should not break
                self.min = self.top.prev_min
            self.top = self.top.next

    # getting (<class 'TypeError'>, TypeError("'Node' object is not callable"), <traceback object at 0x1029b6988>) here not sure why?
    def top(self):
        if self.top:
            return self.top.val
        else:
            return None  # choosing to return None when stack empty

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # return -3
    minStack.pop()
    print(minStack.top())  # return 0# getting (<class 'TypeError'>, TypeError("'Node' object is not callable"), <traceback object at 0x1029b6988>) here
    print(minStack.getMin())  # return -2
