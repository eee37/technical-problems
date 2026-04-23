"""
    https://leetcode.com/problems/linked-list-cycle/description/
    #141
    
    Note that in original answer I did not account for scenario where the head is None. The function description didnt
    imply that could be the case but that is a good question to ask in an interview

    Speed: O(n)
    Space: O(1)
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    """
    if head is None or head.next is None:
    :rtype: bool
    """
    if head.next is None:
        return False
    slow = head
    fast = head.next.next
    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False