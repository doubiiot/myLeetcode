class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[2] = 1
        for i in range(3, n+1):
            var = 0
            tmp = 0
            for j in range(2, i):
                tmp = max(j, dp[j]) * (i-j)
                var = max(var, tmp)
            dp[i] = var
        return dp[n]
################
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j, dp[j]) * (i-j))
        return dp[n]
################
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
        return dp[n]
# O(n^2) O(n)

# class Solution:
#     def integerBreak(self, n: int) -> int:
#         dp = [0 for i in range(n+1)]
#         dp[2] = 1
#         for i in range(3, n+1):
#             t = i // 2
#             a = t * max(dp[i-t], i-t)
#             b = (i-t-1) * max(dp[t+1], t+1)
#             dp[i] = max(a, b)
#         return dp[n]

