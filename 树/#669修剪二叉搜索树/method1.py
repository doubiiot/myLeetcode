# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(root):
            if not root: return None
            elif root.val < low:
                return trim(root.right)
            elif root.val > high:
                return trim(root.left)
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
                return root
        return trim(root)
# Time：O(n)
# Space O(N)