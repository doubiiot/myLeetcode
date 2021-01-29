#中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node_list = []
        def dfs(root):
            if not root: return None
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)
        dfs(root)
        return node_list[k-1]
# TIME O(N)
# SPACE O(N)