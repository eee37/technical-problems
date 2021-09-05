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

    def push(self, val) -> int:
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

if __name__ == '__main__':
    Stack = Stack()
    Stack.push(-2)
    Stack.push(0)
    Stack.push(-3)
    print(Stack.pop())