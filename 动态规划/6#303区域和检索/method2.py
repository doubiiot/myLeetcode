class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i-1]
    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - self.nums[i-1] if i else self.nums[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
