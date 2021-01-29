class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        dp = [0 for i in range(n)]
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i-1] + grid[0][i]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][0]
                else:
                    tmp = dp[j]
                    dp[j] = grid[i][j] + min(dp[j-1], tmp)
        return dp[n-1]
#O(mn) O(n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        dp = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j]
                elif i == 0:
                    dp[j] = dp[j-1]
                else:
                    tmp = dp[j]
                    dp[j] = min(dp[j-1], tmp)
                dp[j] += grid[i][j]
        return dp[n-1]
