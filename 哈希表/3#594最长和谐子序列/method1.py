class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #11.27
        dic = {}
        for val in nums:
            dic[val] = dic.get(val, 0) + 1
        max_length = 0
        for val in nums:
            if dic.get(val+1, 0) != 0:
                max_length = max(dic.get(val+1, 0) + dic.get(val, 0), max_length)
        return max_length
