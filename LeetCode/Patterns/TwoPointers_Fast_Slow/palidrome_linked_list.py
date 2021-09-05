# ******************* PROBLEM STATEMENT

# ******************* NOTES
# 1. First attempt over-complicates problem. Creates complicated sol that produces same efficiency of simpler solution. Question solution before digging deep. See approach # 1
# 2. Approach 3 produces a more optimal answer (similar to what I was originally trying to accomplish) by not reducing storage

# pythonic way of reversing list x[::-1]
# ******************* SOLUTION
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head:
            slow = head
            fast = head.next
            tracker = [slow.val]
            if fast:
                # Make fast point to last
                while slow and fast: # Note: Needed to be fast not fast.next to prevent errors in odd case
                    if not fast.next: # even case
                        # tracker.pop() # get rid of last element
                        break
                    slow = slow.next
                    tracker.append(slow.val)
                    fast = fast.next.next
                if not fast: # odd case
                    tracker.pop()
                    slow = slow.next
                # verify is palindrone
                # walk back verifying is palindrone
                index = len(tracker) - 1
                while slow and index >= 0: # Note: need to increment by one to start assert
                    if slow.val != tracker[index]:
                        return False
                    slow = slow.next
                    index -= 1
                return True

            else:
                # case: one node
                return True
        else:
            return True # case: head is None

    def isPalindromeEasy(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        index = 0
        while index < len(arr)/2: # NOTE: Could use python array flip notation to check instead vals == vals[::-1]
            if arr[index] != arr[len(arr) - 1 - index]:
                return False
            index += 1
        return True



if  __name__ == '__main__':
    sol = Solution()

    x = ListNode(1)
    x.next = ListNode(0)
    x.next.next = ListNode(0)
    #assert not sol.isPalindrome(x)
    assert not sol.isPalindromeEasy(x)
    a = ListNode(1)
    a.next = ListNode(2)
    print(sol.isPalindrome(a))
    # assert not sol.isPalindrome(a)
    assert not sol.isPalindromeEasy(a)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(1)
    # assert sol.isPalindrome(a)
    assert sol.isPalindromeEasy(a)