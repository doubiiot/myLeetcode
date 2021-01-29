# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        rslt = []
        def dfs(root):
            if not root:return None
            rslt.append(root.val)
            if root.left:
                # rslt.append(root.left.val)
                dfs(root.left)
            if root.right:
                # rslt.append(root.right.val)
                dfs(root.right)
        dfs(root)
        return rslt
# time：O(N)
# space: O(N)