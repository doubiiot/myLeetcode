# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        node_list = []

        def dfs(root):
            if not root:
                return None
            node_list.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        while root.val in node_list:
            node_list.remove(root.val)
        return min(node_list) if node_list else -1
