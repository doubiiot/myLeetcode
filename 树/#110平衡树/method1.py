# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    def height(self, root):
        stck = []
        if root is not None:
            stck.append((1, root))
        deep = 0
        while stck != []:
            current_deep, head = stck.pop()
            if head is not None:
                deep = max(deep, current_deep)
                stck.append((current_deep + 1, head.left))
                stck.append((current_deep + 1, head.right))
        return deep
    '''
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)