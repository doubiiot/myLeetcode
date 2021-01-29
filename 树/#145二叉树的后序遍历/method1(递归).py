# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        rslt = []
        def dfs(root):
            if not root: return None
            dfs(root.left)
            dfs(root.right)
            rslt.append(root.val)
        dfs(root)
        return rslt
