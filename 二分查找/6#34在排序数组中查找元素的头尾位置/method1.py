class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        def binary_search(l, r, val):
            while l < r:
                mid = l + (r - l) // 2
#二分查找：如果 nums[mid] < val 查找到的应该是第一次出现的位置
#        如果 nums[mid] <= val查找到的应该是最后一次出现的位置
                if nums[mid] < val:
                    l = mid + 1
                else:
                    r = mid
            return l
        left = binary_search(l, r, target)
        right = binary_search(l, r, target+1)-1

        if left >= r or nums[left] is not target:
            return [-1, -1]
        else:
            return [left, max(left,right)]

