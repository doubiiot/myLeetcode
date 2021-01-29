# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_node(node):
            if not node: return 0, 0
            ls, ln = rob_node(node.left)
            rs, rn = rob_node(node.right)
            return node.val+ln+rn, max(ls, ln) + max(rs, rn)
        return max(rob_node(root))
# time o(n)
# space o(n)