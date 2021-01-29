# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_num = sys.maxsize
        pre = -1

        def dfs(root):
            nonlocal min_num
            nonlocal pre
            if not root: return None
            dfs(root.left)
            if pre == -1:
                pre = root.val
            else:
                min_num = min(abs(root.val - pre), min_num)
                pre = root.val
            dfs(root.right)

        dfs(root)
        return min_num
# O(N) O(N)
#除了递归栈以外 没有使用额外的空间


