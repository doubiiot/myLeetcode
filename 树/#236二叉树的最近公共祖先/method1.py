# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = TreeNode(0)
        def dfs(root, p, q):
            nonlocal node
            if not root:return False
            l_left = dfs(root.left, p, q)
            l_right = dfs(root.right, p, q)
            if (l_left and l_right) or ((root.val == p.val or root.val == q.val) and (l_left or l_right)):
                node = root
            return l_left or l_right or root.val == p.val or root.val == q.val
        dfs(root, p, q)
        return node
# 递归 O(N) O(N)