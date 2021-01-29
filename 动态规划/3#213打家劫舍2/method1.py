class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        #rob 1
        cur1 = cur2 = nums[0]
        for i in range(2, n-1):
            cur1, cur2 = cur2, max(nums[i]+cur1, cur2)
        va1 = cur2
        #rob 2
        cur1, cur2 = nums[1], max(nums[1], nums[2])
        for i in range(3, n):
            cur1, cur2 = cur2, max(nums[i]+cur1, cur2)
        return max(va1, cur2)
# O(n) O(1)
# 也可以用一个函数来表示

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def rob(l, r):
            cur1, cur2 = nums[l], max(nums[l], nums[l+1])
            for i in range(l+2, r):
                cur1, cur2 = cur2, max(nums[i]+cur1, cur2)
            return cur2
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        return max(rob(0, n-1), rob(1, n))







