class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, left, right):
            if left > right:
                return None
            i, j = left, right
            while i != j:
                while nums[j] >= nums[left] and j > i: j -= 1
                while nums[i] <= nums[left] and j > i: i += 1
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    nums[i], nums[left] = nums[left],nums[i]
            quick_sort(nums, left, i-1)
            quick_sort(nums, i+1, right)
            return nums
        nums = quick_sort(nums, 0, len(nums)-1)
        return nums[-k]