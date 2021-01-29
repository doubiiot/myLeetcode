class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m < n:
            # m, n = n, m
        dp = [1 for i in range(n)]
        for i in range(1,m):
            for j in range(n):
                if j != 0:
                    dp[j] += dp[j-1]
        return dp[n-1]
#O(mn) O(n)
