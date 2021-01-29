# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        node_list = []
        def dfs(root):
            if not root:return None
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)
        dfs(root)
        for idx, i in enumerate(node_list):
            if (k-i) in node_list[idx+1:]:
                return True
        return False
# O(N^2) O(n)
