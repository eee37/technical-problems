# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while odd and even:
            odd_next = even.next
            if odd_next:
                even_next = odd_next.next
            else:
                even_next = None
                break
            odd.next = odd_next
            odd = odd_next

            even.next = even_next
            even = even_next

        odd.next = even_head  # w.o break in if statement breaks in the case linked list is even
        return head