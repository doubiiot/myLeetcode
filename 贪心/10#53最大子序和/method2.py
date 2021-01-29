class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = nums[0]
        max_num = pre
        for i in range(1, len(nums)):
            cur = max(pre + nums[i], nums[i])
            if max_num < cur:
                max_num = cur
            pre = cur
        return max_num
# 改进2

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, max_num = 0, nums[0]
        for i in nums:
            cur = max(pre + i, i)
            if max_num < cur:
                max_num = cur
            pre = cur
        return max_num
#再改进
