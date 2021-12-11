from typing import Optional
from DataStructures.linked_list import LinkedListHelper

'''
    LC # 143
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reorderList(head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        pointer1 = head
        pointer2 = head

        # race to end
        while pointer2 and pointer2.next:  # if 1st condition is false does it check second
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        # single node
        if pointer1 == pointer2:
            return

        # reverse 2nd halve
        prev = None  # NOTE: Needs to be orginially be set as None
        curr = pointer1
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # NOTE: Both lists will end in middle node
        # rearrange. TODO: Problem 21
        head1 = head
        head2 = prev  # will at most longer by at least 1

        while head2.next:
            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head2.next = nxt1

            head1 = nxt1
            head2 = nxt2

        # The commented out code below causes an infinite loop. seems to be performed in a concurrent thread as one of the while loops. weird?
        # if head2:
        #     head1.next = head2
        return head

if __name__ == "__main__":
    # head = LinkedListHelper.convert([1,2,3,4])
    # LinkedListHelper.print_list(Solution.reorderList(head))

    head2 = LinkedListHelper.convert([1,2,3,4,5])
    LinkedListHelper.print_list(Solution.reorderList(head2))