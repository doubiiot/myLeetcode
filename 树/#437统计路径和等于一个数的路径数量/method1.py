# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, sumlist):
            if not root: return 0
            sumlist = [num + root.val for num in sumlist]
            sumlist.append(root.val)
            count = 0
            for i in sumlist:
                # nonlocal sum
                if i == sum: count+=1
            return count  + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root,[])
