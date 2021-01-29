class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = res = 0
        for i in range(len(nums)):
            if nums[i] == 1: r += 1
            else:
                res = max(res, r-l)
                l = r = i
        res = max(res, r-l)
        return res
# O(N) O(1)
