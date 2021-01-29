# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def func(l,r):
            if l == r:
                return [TreeNode(l)]
            if r < l:
                return [None]
            rslt = []
            for i in range(l, r+1):
                left_list = func(l, i-1)
                right_list = func(i+1, r)
                for left_tree in left_list:
                    for right_tree in right_list:
                        node = TreeNode(i)
                        node.left = left_tree
                        node.right = right_tree
                        rslt.append(node)
            return rslt
        if n == 0:
            return []
        return func(1,n)
