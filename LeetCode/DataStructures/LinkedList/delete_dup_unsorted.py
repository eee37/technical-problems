# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

from DataStructures.linked_list import ListNode


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if head is None:
            return

        # mark duplicates
        cur = head
        hashmap = defaultdict(lambda: -1)

        while cur:
            if hashmap[cur.val] != -1:
                hashmap.update({cur.val: 2}) # NOTE: [SyntaxError] update is method name to put
            else:
                hashmap.update({cur.val: 1})
            cur = cur.next

        a = None
        b = head

        while b:
            if hashmap[b.val] == 2:
                if a:
                    a.next = b.next
                    b = a.next
                else:
                    head = b.next
                    a = None
                    b = head
            else:
                a = b
                b = b.next

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ONLY REMOVES THE DUPLICATE AND NOT THE ORGIGNAL
from collections import defaultdict
class Solution:
    def onlyDeleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if head is None:
            return

        tracker = set()
        cur = head
        prev = None

        while cur:
            if cur.value in tracker: # NOTE: Python Set Syntax. Check if value in set
                if prev:
                    prev.next = cur.next
                    cur = prev.next

                else:
                    head = cur.next
                    prev = None
                    cur = head
            else:
                tracker.add(cur.value) # NOTE: Python Set Method. Add to a set
                prev = cur
                cur = cur.next
        return head

