class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(l, r, flag):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] > target or (flag and nums[mid] == target):
                    r = mid
                else:
                    l = mid + 1
            return l
        l, r = 0, len(nums)
        l_idx = binary_search(l, r, True)
        if l_idx >= len(nums) or nums[l_idx] != target:
            return [-1, -1]

        return [l_idx, binary_search(l, r, False)-1]


