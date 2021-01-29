class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            if cur >= 0:
                count = 1
                p = q = cur
                while nums[p] != cur:
                    p = nums[p]
                    nums[q] = -1
                    q = p
                    count += 1
                res = max(count, res)
        return res
# O(n) O(1)
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            count, j = 0, i
            while nums[j] != -1:
                count += 1
                p = nums[j]
                nums[j] = -1
                j = p
            res = max(count, res)
        return res
