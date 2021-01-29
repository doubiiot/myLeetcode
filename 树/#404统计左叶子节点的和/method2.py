# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    right_flag = 1

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0

        if self.right_flag == 0 and root.left == None and root.right == None:
            return root.val

        if root and root.left:
            self.right_flag = 0
            sum += self.sumOfLeftLeaves(root.left)

        if root and root.right:
            root = root.right
            self.right_flag = 1
            sum += self.sumOfLeftLeaves(root)

        return sum
