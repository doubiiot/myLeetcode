# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归方法 o(n),o(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:return root
        #root.left,root.right=root.right,root.left
        node = TreeNode(0)
        node = root.left
        root.left = root.right
        root.right = node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
