# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#中序94，前序144，后序145
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stk, rslt = [], []
        prev = None
        while root or len(stk) != 0:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if not root.right or root.right == prev:
                rslt.append(root.val)
                prev = root
                root = None
            else:
                stk.append(root)
                root = root.right
        return rslt
# Time O(N)
# SPACE avg O(logn) worse O(n)
