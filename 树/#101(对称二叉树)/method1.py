# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetricTree(self, s ,t):
        if not s and not t:return True
        if (not s and t) or (not t and s):return False
        if s.val != t.val:return False
        else:
            return self.isSymmetricTree(s.left,t.right) and self.isSymmetricTree(s.right,t.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:return True
        return self.isSymmetricTree(root.left, root.right)
#time O(n)
#space O(n)