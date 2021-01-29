class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #11.25
        hashtable = {}
        for idx, val in enumerate(nums):
            if target - val in hashtable:
                return [hashtable[target - val], idx]
            hashtable[val] = idx
        return []

