# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node_stack,rslt = [root],[]
        while node_stack:
            node = node_stack.pop()
            if node:
                rslt.append(node.val)
                if node.right:
                    node_stack.append(node.right)
                if node.left:
                    node_stack.append(node.left)
        return rslt
    # 中序94，前序144，后序145
# time: O(N)
# space: O(N)
