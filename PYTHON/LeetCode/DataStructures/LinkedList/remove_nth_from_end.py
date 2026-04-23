"""
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/editorial/
    #19
    Struggled implementing this one.
    Key is that want pointers to be n nodes apart so that left pointer's next node is the one to be deleted
    Left pointer needs to be 1 behind to make deleting possible in one pass
    The use of a dummy node at the beginning enables to solve the base case -> 1 node
    Also need to realize that in the end right will be None. Right past the tail node
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_node(self):
        node = self
        print_statement = 'start -> '
        while node is not None:
            print_statement += '->' + str(node.val)
            node = node.next
        print(print_statement + ' -> end')


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head

    @staticmethod
    def print_node(node: ListNode):
        print_statement = ''
        while node is not None:
            print_statement += '->' + str(node.val)
            node = node.next
        print(print_statement)

class LinkedListFromList:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.head = None
        curr = None
        for index, num in enumerate(arr):
            new_node = ListNode(num)
            if curr:
                curr.next = new_node
            curr = new_node
            if index == 0:
                self.head = curr


    def print_list(self):
        node = self.head
        print_statement = 'null ->'
        while node is not None:
            print_statement += '->' + str(node.val)
            node = node.next
        print(print_statement + '-> null')


def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    dummy = ListNode(next=head)
    left = dummy
    right = dummy

    for _ in range(n+1):
        right = right.next
    
    while right != None:
        left = left.next
        right = right.next
    left.next = left.next.next

    return dummy.next

test = LinkedListFromList([1,2,3,4,5]).head
result = removeNthFromEnd(test, 2)
result.print_node()
        
        