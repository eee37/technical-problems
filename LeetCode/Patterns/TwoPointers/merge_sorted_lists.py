# ******************* PROBLEM STATEMENT
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
# ******************* NOTES
# Solution uses "and" in while loop to append end of final remaining linked list to merged list and save code lines
# Solution uses dummy head node to save code lines

# ******************* SOLUTION
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # Note: Optional[x] = UNION[x, None] meaning either type x or None is valid
        head = None
        prev = None # NOTE: Need to keep pointers of prev and next to append next node to the prev in all scenarios
        while l1 or l2:
            if l2 and not l1:
                next = l2
                l2 = l2.next
            elif l1 and not l2:
                next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    next = l1
                    l1 = l1.next
                else:
                    next = l2
                    l2 = l2.next
            if not head:
                head = next
            else:
                prev.next = next
            prev = next
        return head
