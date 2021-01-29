class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        dp = [0] * (n+1)
        for i in range(4, n+1):
            dp[i] = max(2*(i-2), 2*dp[i-2], 3*(i-3), 3 * dp[i-3])
        return dp[n]
#O(n) O(n)
