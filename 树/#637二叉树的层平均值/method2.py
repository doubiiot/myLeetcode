# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# BFS
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return None
        rslt_list = []
        queue = collections.deque([root])
        while queue:
            node_num = len(queue)
            val = 0
            for i in range(node_num):
                node = queue.popleft()
                val += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rslt_list.append(val/node_num)
        return rslt_list