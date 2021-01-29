class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur = 0
        for i in range(k):
            for j in range(n-i-1):
                if nums[j] >= nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[-k]
