# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        cur, number, max_num, rslt = None, 0, 0, []
        def dfs(root):
            nonlocal cur,number,max_num,rslt
            if not root: return None
            dfs(root.left)
            if cur == 0:
                cur == root.val
            if cur == root.val:
                number += 1
            else:
                cur = root.val
                number = 1
            if number > max_num:
                max_num = number
                rslt = [root.val]
            elif number == max_num:
                rslt.append(root.val)
            dfs(root.right)
        dfs(root)

        return rslt
# O(N) O(N)
# 优化 除了返回的结果和隐式栈之外没有调用额外的空间
