# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#遍历
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:return root
        stck = []
        stck.append(root)
        while stck:
            node = stck.pop()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:stck.append(node.left)
            if node.right:stck.append(node.right)
        return root



