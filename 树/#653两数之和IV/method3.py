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
            nonlocal node_list
            if not root:return None
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)
        dfs(root)
        left, right = 0, len(node_list)-1
        while left < right:
            cur = node_list[left] + node_list[right]
            if cur == k: return True
            elif cur < k: left += 1
            elif cur > k: right -= 1
        return False