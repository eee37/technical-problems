class BinaryTreeNode:
    def __init__(self, v=None, l=None, r=None):
        self.v=v
        self.l=l
        self.r=r

        self.value=v
        self.left=l
        self.right=r

# From https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
class newNode:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None
 
# Function to insert nodes in level order
def insertLevelOrder(arr, root: BinaryTreeNode, i, n):
    # Base case for recursion
    if i < n:
        temp = newNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                    2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                    2 * i + 2, n)
    return root