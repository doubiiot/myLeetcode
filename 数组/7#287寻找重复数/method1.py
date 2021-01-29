class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                return num
            else:
                dic[num] = 1
        return 0
# 不合题意
# 哈希表解法 O(n) O(n)
