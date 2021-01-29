class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, end = 0, n - 1
        while i < end:
            if nums[i] != 0: i += 1
            else:
                j = i
                while j < end:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j += 1
                end -= 1


