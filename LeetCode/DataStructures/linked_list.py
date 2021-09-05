# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


