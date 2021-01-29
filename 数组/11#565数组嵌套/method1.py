class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        dic, res = {}, 0
        for i in range(len(nums)):
            cur = nums[i]
            if cur not in dic:
                count, temp = 1, cur
                while nums[temp] != cur:
                    temp = nums[temp]
                    count += 1
                    dic[temp] = 1
                res = max(count, res)
        return res
# O(n) O(n)
