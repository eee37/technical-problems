'''
******************* PROBLEM STATEMENT

******************* NOTES
1. RECURSIVE SOLN: Trick to understanding recursive soln' is that the value for right is passed down recursively so after last recursive step it backtracks
while value for left is shared and after last recursive steps is evaluate to next node. and they march towards each other until thye meet terminating condition
2. LL TRAVERSAL SOLUTION (gotcha): Link to left node is inverted even though its not suppose to but in final part its set correctly
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)

******************* SOLUTION
'''

# Definition for singly-linked list.
from DataStructures.linked_list import LinkedListFromList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def print_node(self):
        node = self
        print_statement = 'start -> '
        while node is not None:
            print_statement += '->' + str(node.val)
            node = node.next
        print(print_statement + ' -> end')

from typing import Optional


class Solution:
    '''
        NOTE:
            1) Third pointer not needed in this solution
            2) Need to use left to determine how to rearrange subarrray within larger array

    '''
    @staticmethod
    def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        # init trackers
        prev = None
        curr = head
        counter = 1
        # allow cur to reach left node
        while counter <= left:
            if counter == left - 1:
                sub_tail_prev = curr
            if counter == left:
                sub_tail = curr
            prev = curr
            curr = prev.next
            counter += 1
        # allow cur to reach curr node
        while left < counter <= right:
            temp_curr = curr.next

            # flip
            curr.next = prev

            prev = curr
            curr = temp_curr
            counter += 1

        # re-arrange subarray
        if left > 1:
            sub_tail_prev.next = prev
        else:
            head = prev

        sub_tail.next = curr

        return head




    def reverseBetweenOne(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return head

        counter = 1
        prev = None
        curr = head
        skip = curr.next

        while curr:
            if counter == left - 1:
                left_tail = curr
            elif counter >= left and counter <= right:
                curr.next = prev
            if count == left:
                left_node = curr
            if count == right:
                break
            counter += 1

            # update pointers
            prev = curr
            curr = skip
            if skip:
                skip = skip.next

        if left == 1:
            head = curr
        else:
            left_tail.next = curr
            left_node.next = skip

if __name__ == '__main__':
    linked_list = LinkedListFromList([1,2,3,4,5])
    linked_list.print_list()
    Solution.reverseBetween(linked_list.head, 2, 4).print_node()