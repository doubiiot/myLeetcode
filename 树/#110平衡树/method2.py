# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalancedTool(self,root):
        if root is None:
            return True,-1
        left_is_balance,left_height = self.isBalancedTool(root.left)
        if not left_is_balance:
            return False,0

        right_is_balance,right_height = self.isBalancedTool(root.right)
        if not right_is_balance:
            return False,0
        return abs(left_height-right_height) < 2 , max(left_height,right_height)+1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedTool(root)[0]
