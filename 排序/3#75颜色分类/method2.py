class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur, length = 0, len(nums)
        for i in range(length):
            if nums[i] == 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1
        for i in range(cur, length):
            if nums[i] == 1:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1
# O(N),O(1)
