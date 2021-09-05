from DataStructures.linked_list import ListNode, LinkedList

'''
        Notes:
            1. Determining condition in while/if conditions was the hardest part. Took several attempts. Converting them to the save base index helped (i.e. 1 to 0-based index)
        Complexities:
            Time: O(n)
            Space: O(1)
'''

class Solution:
    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

        cur = head
        count = 0
        # count nodes
        while cur:
            cur = cur.next
            count += 1

        # find kth from end node and delete
        if n > count + 1 or n <= 0:
            return head

        # case where need to delete head. NOTE: Both are 1-index based
        if count == n:
            head = head.next
            return head

        cur = head # will be set to node before one needed to be deleted
        index = 0

        print(count)
        while index < count - 1 - (n-1) - 1: # NOTE: Need to use '<' bc the prev iter will set to node where condition is met cuz of cur = cur.next. Conver all to 0-index based
            cur = cur.next
            index += 1
        # CtCI 2.2 return cur
        cur.next = cur.next.next
        print(count)
        LinkedList.print_node(head)

        return head

if __name__ == '__main__':
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    # Solution.removeNthFromEnd(head, 2)

    head = ListNode(1, None)
    Solution.removeNthFromEnd(head, 1)

    head = ListNode(1, ListNode(2, None))
    Solution.removeNthFromEnd(head, 1)