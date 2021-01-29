class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for j in range(n):
            for i in range(j+1):
                if i+1 <= j-1:
                    dp[i][j] = dp[i+1][j-1] & (s[i]==s[j])
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 1
        res = 0
        for j in range(n):
            res += sum(dp[j])
        return res


       
