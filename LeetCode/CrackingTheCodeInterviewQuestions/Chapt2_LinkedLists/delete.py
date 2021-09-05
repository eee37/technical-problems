from DataStructures.linked_list import ListNode # How does file paths work in python


class Solution:
    @staticmethod
    def deleteNode(node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # if node and node.next: # NOTE: This doesnt work cause node is only defined in the context of the fxn. this only updates the ref to the object node in the context of this fxn outside of this fxn ref don't change
        #     node = node.next

        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next


