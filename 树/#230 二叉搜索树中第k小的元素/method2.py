# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stk = []
        while True:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
# Time O(H + k) WORSE O(N+k) BSET O(logN + k)
# Space same with top