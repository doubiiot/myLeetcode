#方法二改进
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_sum = sum(nums)
        nums_max = max(nums)
        target = nums_sum // 2
        if n < 2 or nums_sum & 1 or nums_max > target:
            return False
        dp = [False for _ in range(target+1)]
        dp[0] = True

        for i in range(0, n):
            num = nums[i]
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[target]
