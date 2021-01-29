# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        #求节点的最长深度
        def helper(root):
            if not root: return 0
            left_length = helper(root.left)
            right_length = helper(root.right)
            # 边长
            left = right = 0
            if root.left and root.left.val == root.val:
                left = 1 + left_length
            if root.right and root.right.val == root.val:
                right = 1 + right_length
            # 当前节点最长深度与全局最长深度对比
            self.ans = max(self.ans, left+right)
            return max(left, right)
        helper(root)
        return self.ans