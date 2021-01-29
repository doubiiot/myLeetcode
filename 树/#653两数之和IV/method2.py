# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        dic = {}
        def dfs(root):
            if not root:return False
            if (k-root.val) in dic:
                return True
            else:
                dic[root.val] = 0
            return dfs(root.left) or dfs(root.right)
        return dfs(root)


#dic好像比list快一些