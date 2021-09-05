'''
******************* PROBLEM STATEMENT

******************* NOTES

is: pythonic way of checking for equality of objects
in: can be used in conditional to determine if item in list
When dealing with linked lists make sure to check for null pointer exceptions!

TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: 0

******************* SOLUTION
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        if head: # NOTE: BASE CASE: head is None
            while slow.next:
                if fast.next is None or fast.next.next is None:
                    return False # NOTE: Fast reaches last node, note that fast will always reach last node first
                slow = slow.next
                fast = fast.next.next
                if slow is fast: # NOTE: Don't just want to check value. Need to check that they point to same object
                    return True
        return False


class Solution:
    def hasCycleHash(self, head: ListNode) -> bool:
        if head is None:
            return False
        nodes = set() # NOTE: Python way of initializing set, only accepts iterable as input to create set from input
        nodes.add(head)
        while head.next:
            head = head.next
            if head in nodes: # NOTE: Python Syntax for checking if element in array
                return True
            nodes.add(head)
        return False
