# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_list = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)
        def construct_tree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(node_list[mid])
            root.left = construct_tree(left, mid-1)
            root.right = construct_tree(mid+1, right)
            return root
        dfs(root)
        node = construct_tree(0, len(node_list)-1)
        return node

