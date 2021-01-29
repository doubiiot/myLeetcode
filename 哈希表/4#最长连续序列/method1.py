class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        res = 1
        max_length = res
        for i in range(n-1):
            if nums[i] + 1 == nums[i+1]:
                res += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                max_length = max(res, max_length)
                res = 1
        max_length = max(res, max_length)
        return max_length


