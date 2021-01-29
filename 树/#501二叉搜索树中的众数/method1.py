# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        node_list = []
        dic = {}
        def dfs(root):
            if not root: return None
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)
        dfs(root)
        for i in node_list:
            dic[i] = dic.get(i,0) + 1
        num = 0
        rslt = []
        for k,v in dic.items():
            if v > num:
                rslt = [k]
                num = v
            elif v == num:
                rslt.append(k)
        return rslt
# O(N) O(N)