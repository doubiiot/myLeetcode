# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        rslt, stk = [], []
        while root or len(stk) > 0:
            while root:
                stk.append(root)
                root = root.left
            #left mid right
            root = stk.pop()
            rslt.append(root.val)
            root = root.right
        return rslt
# 中序94，前序144，后序145
# TIME O(N)
# SPACE O(N)