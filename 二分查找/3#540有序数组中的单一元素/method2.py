class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while True:
            if l == r:
                return nums[l]
            mid = l + (r - l) // 2
            if nums[mid] == nums[mid+1]:
                if (mid - l) % 2 != 0:
                    r = mid - 1
                else:
                    l = mid + 2
            elif nums[mid] == nums[mid-1]:
                if (r - mid) % 2 != 0:
                    l = mid + 1
                else:
                    r = mid - 2
            else:
                return nums[mid]


