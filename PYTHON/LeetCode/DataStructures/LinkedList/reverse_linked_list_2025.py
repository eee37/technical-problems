"""
https://leetcode.com/problems/reverse-linked-list/description/
#206
My while condition was off in the first attempt. used  current.next is not None which meant while block was skipped on last node

TIME: O(n)
SPACE: O(1)
"""

def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    current = head
    prev = None


    while current is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

two = ListNode(2)
one = ListNode(1, two)


print(reverseList(one).__dict__)
