# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSametree(self,s,t):
        if not s and not t:return True
        if (not s and t) or (not t and s) or (s.val != t.val):return False
        else:
            return self.isSametree(s.left,t.left) and self.isSametree(s.right,t.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s : return False
        return self.isSametree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
# time O(|s| * |t|)
# space O(max(|s|,|t|))
