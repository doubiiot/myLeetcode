class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, i: int, j: int) -> int:
        self.cur = sum(self.nums[i:j+1])
        return self.cur

#O(mn) O(1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
