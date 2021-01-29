class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: return nums[0]
        else:
            slow, quick = 0, 1
            while quick < length:
                if nums[slow] == nums[quick]:
                    slow += 2
                    quick += 2
                else:
                    return nums[slow]
            return nums[slow]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums)-2,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
