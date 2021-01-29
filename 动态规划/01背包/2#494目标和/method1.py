class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        #11.24
        if S > 1000 or S < -1000:
            return 0
        n = len(nums)
        dp = [[0] * 2001 for _ in range(n)]
        dp[0][1000 + nums[0]] += 1
        dp[0][1000 - nums[0]] += 1
        for i in range(1,n):
            num = nums[i]
            for j in range(0, 2001):
                a = dp[i-1][j-num] if j - num > 0 else 0
                b = dp[i-1][j+num] if j + num <= 2000 else 0
                dp[i][j] = a + b
        return dp[n-1][1000+S]
