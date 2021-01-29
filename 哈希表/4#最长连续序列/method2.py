class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashtable = {}
        res = 0
        count = 1
        for num in nums:
            hashtable[num] = hashtable.get(num,0) + 1
        for i in range(len(nums)):
            #hashtable[nums[i]] = hashtable.get(nums[i], 0) + 1
            if not hashtable.get(nums[i]-1, 0):
                num = nums[i]+1
                while hashtable.get(num, 0):
                    count += 1
                    num += 1
                res = max(res, count)
                count = 1
        return res


