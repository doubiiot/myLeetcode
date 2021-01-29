class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #11.26
        hashtable = {}
        for idx, num in enumerate(nums):
            if num in hashtable:
                return True
            hashtable[num] = 0
        return False
