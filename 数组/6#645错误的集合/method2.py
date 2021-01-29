class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num)-1] < 0:
                dup = abs(num)
            else:
                nums[abs(num)-1] *= -1
        for idx, num in enumerate(nums):
            if num > 0:
                lost = idx + 1
                break
        return [dup, lost]

#O(n) O(1)
