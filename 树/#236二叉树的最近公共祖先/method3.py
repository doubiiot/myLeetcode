# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father_dic = {}
        vis_dic = {}

        def dfs(node, father):
            nonlocal father_dic
            if not node: return False
            father_dic[node] = father
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        while p:
            vis_dic[p] = True
            p = father_dic[p]
        while q:
            if vis_dic.get(q, 0) != 0:
                return q
            else:
                q = father_dic[q]


# 记录父节点
# O(N) O(N)