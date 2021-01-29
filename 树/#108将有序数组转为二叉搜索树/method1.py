# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None
        mid_idx = length // 2
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[0:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root
# 主要思想：取中间节点，递归中序遍历
# Time O(N^2)
# Space O(logN)