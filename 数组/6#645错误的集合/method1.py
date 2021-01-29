class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)
        num = min(nums)
        for i in range(n):
            if nums[i] in dic:
                rpte = nums[i]
            else:
                dic[nums[i]] = 1
        for i in range(1, n+1):
            if i not in dic:
                lost = i
                break
        return [rpte, lost]
#O(n) O(n)
