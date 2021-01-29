class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                cur_num = num
                count = 1
                while cur_num+1 in nums:
                    cur_num += 1
                    count += 1
                res = max(res, count)
        return res
