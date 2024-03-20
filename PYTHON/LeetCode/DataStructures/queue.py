class Queue:
    '''
        Implementation varies on order
            first/head -> last/tail or last/tail -> first/head
        The first doesnt require prev tracker
    '''
    class QueueNode:
        def __init__(self, val: int, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val) -> int:
        new_head = self.QueueNode(val, self.head, None)
        if self.head:
            self.head.prev = new_head
        else: # if no head then also no tail
            self.tail = new_head
        self.head = new_head
        return val


def pop(self) -> int:
    if not self.tail:
        return None
    val = self.tail.val

    self.tail = self.tail.prev

    if self.tail:  # case where tail is not none, was not single node queue
        if not self.tail.prev:  # case where now a single node remains, need to update head
            self.head = self.tail

    self.tail.next = None

    return val


def peek(self) -> int:
    if self.tail:
        return self.tail.val
    else:
        return None


def is_empty(self):
    return self.tail is None and self.head is None  # should be sufficient to chec one


