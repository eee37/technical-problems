'''
        Learnings:
            1. Misinterpreted problem. READ PROBLEM STATEMENT CAREFULLY
            2. Leetcode problem different from textbook. Leetcode its ordered
            3. Not learning from prev errors
            4. Can use fact that None is Falsy in conditionals
            5. Set time limit to avoid rabbit holes

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    @staticmethod
    def deleteDuplicates( head: ListNode) -> ListNode:
        # sort linked list
        current = head
        values = []

        while current != None:
            values.append(current.val)
            current = current.next  # insert?

        sorted_values = sorted(values)

        pointer = 0
        current = head
        prev = None

        print(sorted_values)

        while pointer < len(sorted_values):  # it is stuck in this while loop
            if sorted_values[pointer] != current.val:
                tracker = current
                while tracker.val != sorted_values[pointer]:
                    tracker =  tracker.next
                if pointer != 0:
                    prev.next = tracker
                    tracker.next = current
                else:
                    head = tracker
                    prev = tracker
                    tracker.next = current
                pointer += 1
                continue # dont want to update current
            elif sorted_values[pointer] == current.val and pointer == 0:
                prev = current

            current = current.next
            pointer += 1

        current.next = None

        Solution.print_node(head) # cut off 2

        # remove duplicates
        current = head
        prev = None
        while current is not None:
            if current.val == current.next.val:
                if prev is None: # current is head
                    head = current.next
                    prev = head
                else:
                    prev.next = current.next
                current = current.next.next
            else:
                prev = current
                current = current.next
        
        Solution.print_node(head)
        return head
                    
    @staticmethod
    def print_node(node: ListNode):
        print_statement = ''
        while node is not None:
            print_statement += node.val
            node = node.next
        print(print_statement)


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(1, None)))
    Solution.deleteDuplicates(head)