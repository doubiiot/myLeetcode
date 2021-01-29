class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def func(val):
            count = 0
            for num in nums:
                if num <= val:
                    count += 1
            #说明val这个数在target之前
            return count <= val
        l, r = 1, len(nums)-1
        while l < r:
            mid = l + (r - l) // 2
            if func(mid):
                l = mid + 1
            else:
                r = mid
        return l
# 二分查找做法(符合题意)
# 设目标值为 target
# 对于小于target的值，cnt[i] <= i
# 对于大于target的值，cnt[i] > i
# O(nlogn) O(1)
