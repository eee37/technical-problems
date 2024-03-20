'''
    NOTE:
            1) Misunderstood problem as unsorted original at first
            2) Dummy node strategy can be used here
'''

from collections import defaultdict

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        cur = head
        tracker = defaultdict(lambda: -1)

        id = 0
        while cur:
            id += 1
            if tracker[cur.val] == -1:
                tracker.update({cur.val: 1})
            else:
                tracker.update({cur.val: 2})
            cur = cur.next

        # NOTE: Python Method. Use key param to tell python how to sort nodes.sort(key=lambda tup: tup[1])

        prev = None
        cur = head
        new_head = None

        while cur:
            if tracker[cur.val] != 2:
                if prev is None:
                    new_head = cur
                else:
                    prev.next = cur
                prev = cur
            else:
                if prev is not None:
                    prev.next = None
            cur = cur.next
        return new_head

