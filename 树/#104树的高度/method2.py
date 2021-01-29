# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stk = []
        if root is not None:
            stk.append((1, root))

        deep = 0
        while stk != []:
            current_depth, head = stk.pop()
            if head is not None:
                deep = max(deep, current_depth)
                stk.append((current_depth + 1, head.left))
                stk.append((current_depth + 1, head.right))
        return deep
