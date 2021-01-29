# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#迭代
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:return t2
        stack = []
        stack.append([t1,t2])
        while stack:
            node1,node2 = stack.pop()
            if not node1 or not node2:continue
            node1.val += node2.val

            if node1.left is None: node1.left = node2.left
            else: stack.append([node1.left,node2.left])

            if node1.right is None: node1.right = node2.right
            else: stack.append([node1.right,node2.right])

        return t1