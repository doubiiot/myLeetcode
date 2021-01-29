class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:return n
        up, down = 1, 1
        for i in range(1,n):
            if nums[i] - nums[i-1] > 0:
                up = max(down + 1, up)
            elif nums[i] - nums[i-1] < 0:
                down = max(up + 1, down)
        return max(up, down)


