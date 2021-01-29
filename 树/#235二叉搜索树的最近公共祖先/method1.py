# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(root, node):
            path_list = []
            while root != node:
                path_list.append(root)
                if root.val > node.val:
                    root = root.left
                elif root.val < node.val:
                    root = root.right
            path_list.append(node)
            return path_list
        path_a = get_path(root, p)
        path_b =  get_path(root, q)
        ancestor = 0
        for u,v in zip(path_a, path_b):
            if u == v:
                ancestor = u
            else:
                break
        return ancestor
# Time O(N)
# Space O(N)