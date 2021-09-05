'''
Lessons:
    1. LIMIT TIME SPENT ON PROBLEM
Notes:
    1. Required Hint #2 to solve problem. Need to see catch to solve. Requires ingenuity
    2. Couldn't answer optional Hint #2 question

    Hints #98
The major difference between a queue and a stack is the order of elements. A queue
removes the oldest item and a stack removes the newest item. How could you remove
the oldest item from a stack if you only had access to the newest item?
    Hints #114
We can remove the oldest item from a stack by repeatedly removing the newest item
(inserting those into the temporary stack) until we get down to one element. Then, after
we've retrieved the newest item, putting all the elements back. The issue with this is
that doing several pops in a row will require 0 (N) work each time. Can we optimize for
scenarios where we might do several pops in a row?
    A change in one stack needs to be reflected on other stack ow it will run into issues when attempting to re-create a stack
    Maybe by adding a prop stack size and inverted stack size so that when re-creating a stack from another inverted stack, you know where to stop
    Will stop popping when heads next is none (i.e. one node remaining) then would recreated inverted stack from stack stopping at the
    (stack_size - inverted_stack_size)th node. This works cause regular stack can only gain nodes

'''

class MyQueue:
    class Stack:
        '''
        Lesson: In pop and seek need to handle case where head is null
        '''
        class StackNode:
            def __init__(self, val: int, next=None):
                self.val = val
                self.next = next

        def __init__(self, head=None):
            self.head = head

        def push(self, val: int) -> int:
            new = self.StackNode(val, self.head)
            self.head = new
            return val

        def peek(self) -> int:
            return self.head.val if self.head else None  # NOTE: Need to handle case where head is null

        def pop(self) -> int:
            if not self.head: # NOTE: Need to handle case where head is null
                return None
            popped = self.head
            self.head = self.head.next
            return popped.val

        def is_empty(self) -> bool:
            return self.head is None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = self.Stack() # NOTE: Need to use self here because class and initializer are nested
        self.inverted_stack = self.Stack()

    def get_stack(self) -> Stack:
        return self.stack

    def get_inverted(self) -> Stack:
        return self.inverted_stack

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        return self.get_stack().push(x) # NOTE: Only push value bc Stack handles node creation


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element. USING STACK AS SOURCE OF TRUTH. INVERTED STACK IS IN-MEMORY ONLY
        Time: O(2N)
        """
        if  self.stack.is_empty():
            return None
        else:
            # destroy stack and create inverted
            while not self.stack.is_empty():
                self.inverted_stack.push(self.stack.pop())
            to_return = self.inverted_stack.pop()

            # destroy inverted and create stack
            while not self.inverted_stack.is_empty():
                self.stack.push(self.inverted_stack.pop())
            return to_return



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack.is_empty():
            return None
        else:
            # destroy stack and create inverted
            while not self.stack.is_empty():
                self.inverted_stack.push(self.stack.pop())
            to_peek = self.inverted_stack.peek()

            # destroy inverted and create stack
            while not self.inverted_stack.is_empty():
                self.stack.push(self.inverted_stack.pop())
            return to_peek
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.get_stack().is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(-2)
    queue.push(0)
    print(queue.peek())
    print(queue.empty())
    print(queue.pop())
    print(queue.peek())