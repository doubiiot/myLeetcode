# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeafNode(self,node):
        return True if not node.left and not node.right else False
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # isLeafNode = lambda node: not node.left and not node.right
        if not root: return 0
        if root.left and self.isLeafNode(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)