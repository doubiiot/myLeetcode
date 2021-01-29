class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        f = [0] * length
        f[0] = nums[0]
        for i in range(1, length):
            f[i] = max(f[i-1]+nums[i], nums[i])
        return max(f)
