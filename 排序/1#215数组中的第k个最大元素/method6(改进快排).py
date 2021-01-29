import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def random_partition(nums, left, right):
            idx = random.randint(left, right)
            nums[idx], nums[right] = nums[right], nums[idx]
            return partition(nums, left, right)

        def partition(nums, left, right):
            i = left - 1
            pivot = nums[right]
            for j in range(left, right):
                if nums[j] <= pivot:
                    i = i + 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[right] = nums[right], nums[i+1]
            return i+1
        def quick_sort(nums, left, right, loc):
            idx = random_partition(nums, left, right)
            if idx == loc:
                return nums[idx]
            elif idx < loc:
                return quick_sort(nums, idx+1, right, loc)
            else:
                return quick_sort(nums, left, idx-1, loc)
        return quick_sort(nums, 0, len(nums)-1, len(nums)-k)
#改进快排
