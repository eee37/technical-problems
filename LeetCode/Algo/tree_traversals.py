# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# IN-ORDER
from DataStructures.treenode import BinaryTreeNode

visited = []


# NOTE: THIS IS RECURSIVE NOT ITERATIVE
def in_order(node: BinaryTreeNode):
    if not node:
        return
    in_order(node.l)
    visited.append(node.v)
    in_order(node.r)


# POST-ORDER
def post_order(node: BinaryTreeNode):
    if not node:
        return
    post_order(node.l)
    post_order(node.r)
    visited.append(node.v)


# PRE-ORDER
def pre_order(node: BinaryTreeNode):
    if not node:
        return
    visited.append(node.v)
    pre_order(node.l)
    pre_order(node.r)


def print_arr(arr: list):
    [print(node) for node in arr]

'''
            1
    2               3
4       5       None    None

'''
if __name__ == '__main__':
    root = BinaryTreeNode(1)
    root.l = BinaryTreeNode(2)
    root.r = BinaryTreeNode(3)
    root.l.l = BinaryTreeNode(4)
    root.l.r = BinaryTreeNode(5)
    #in_order(root)
    #post_order(root)
    pre_order(root)
    print_arr(visited)
