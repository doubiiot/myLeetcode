class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:

        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, path):
        if not root:
            return 0
        path -= root.val
        return (1 if path == 0 else 0) + self.dfs(root.left, path) + self.dfs(root.right, path)