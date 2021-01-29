# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:return False
        node_list = []
        path_list = []
        node_list.append(root)
        path_list.append(root.val)
        while node_list:
            cur_node = node_list.pop()
            dst = path_list.pop()
            if not cur_node.left and not cur_node.right:
                if dst == sum:return True
                continue
            if cur_node.left:
                node_list.append(cur_node.left)
                path_list.append(dst + cur_node.left.val)
            if cur_node.right:
                node_list.append(cur_node.right)
                path_list.append(dst + cur_node.right.val)
        return False