# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 与637题类似，小改
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        while queue:
            node_num = len(queue)
            flag = 0
            for i in range(node_num):
                node = queue.popleft()
                if flag == 0:
                    left_node = node
                    flag += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return left_node.val