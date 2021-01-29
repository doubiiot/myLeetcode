class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        val = S + sum(nums)
        if sum(nums) < S or val % 2:return 0
        target = val // 2
        dp = [0] * (target+1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] += dp[j-num]
        return dp[target]
