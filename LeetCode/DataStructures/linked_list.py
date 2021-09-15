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


