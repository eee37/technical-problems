'''
******************* PROBLEM STATEMENT

******************* NOTES
1. Main idea is to pass through the list and each step flip the direction of the relationship.
2. In recursive case need to remember to pass along new root plus assign None to last node

******************* SOLUTION
'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # keep pointers at prev, curr and next and reverse curr by reassigning and use next to set next curr
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr  # NOTE: Assign prev before re-assigning curr in the line below
            curr = temp
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ideas:
        # just pass along the last node so that it gets returned
        # in iterative case flip direction of head and head.next, assume everything post head.next has already been flipped

        if not head or not head.next:
            return head
        last = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    test = ListNode(1)
    test.next = ListNode(2)
    sol = Solution()
    print(sol.reverseList(test))
