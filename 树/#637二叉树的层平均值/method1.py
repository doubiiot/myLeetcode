# 深度优先遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return None
        def dfs(root, level):
            if not root: return None
            #层还没有节点
            if level < len(layer_count):
                layer_count[level] += root.val
                num_count[level] += 1
            else:
                layer_count.append(root.val)
                num_count.append(1)
            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)
        layer_count = []
        num_count = []
        dfs(root, 0)
        return [i/j for i,j in zip(layer_count, num_count)]