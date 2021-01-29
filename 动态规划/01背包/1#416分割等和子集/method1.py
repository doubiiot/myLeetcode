class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        sum_val = sum(nums)
        max_num = max(nums)
        target = sum_val // 2
        if length < 2 or sum_val % 2 != 0 or max_num > target:
            return False
        dp = [[False] * (target+1) for _ in range(length)]
        for i in range(length):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for i in range(1, length):
            num = nums[i]
            for j in range(1, target+1):
                #可放可不放
                if j >= num:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - num]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[length-1][target]
# O(m*n) O(m*n)






