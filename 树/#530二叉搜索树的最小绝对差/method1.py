# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        node_list = []

        def dfs(root):
            nonlocal node_list
            if not root: return None
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)

        dfs(root)
        cur = abs(node_list[0] - node_list[1])
        for i in range(1, len(node_list) - 1):
            if abs(node_list[i] - node_list[i + 1]) < cur:
                cur = abs(node_list[i] - node_list[i + 1])
        return cur
# O(N) O(N)
# 方法二优化 不用额外空间


