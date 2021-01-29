# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        rslt = []
        stk = collections.deque()
        while root or len(stk) > 0:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            rslt.append(root.val)
            root = root.right
        return rslt

