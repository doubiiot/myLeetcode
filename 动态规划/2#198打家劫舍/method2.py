class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        front = nums[0]
        rear = max(nums[0], nums[1])
        for i in range(2,n):
            #dp = max(nums[i]+front, rear)
            front, rear = rear, max(nums[i]+front, rear)
        return rear
# O(n) O(1)
