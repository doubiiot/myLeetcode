#自己的做法 记录父节点的值 O(N^2) O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father_dic = {}
        def dfs(node, father, p, q):
            nonlocal father_dic
            if not node:return False
            father_dic[node] = father
            dfs(node.left,node, p, q)
            dfs(node.right,node, p, q)
        def get_list(node):
            path_list = [node]
            while father_dic[node]:
                node = father_dic[node]
                path_list.append(node)
            return path_list
        dfs(root, None, p, q)
        path_a = get_list(p)
        path_b = get_list(q)
        for i in range(len(path_a)):
            for j in range(len(path_b)):
                if path_a[i] == path_b[j]:
                    return path_a[i]