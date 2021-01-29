class Solution:
    def numSquares(self, n: int) -> int:
        lst = [i ** 2 for i in range(1,int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for var in lst:
                if i < var:
                    break
                dp[i] = min(dp[i], dp[i-var] + 1)
        return dp[n]
# O(n * (n ^ 0.5)) O(n)
