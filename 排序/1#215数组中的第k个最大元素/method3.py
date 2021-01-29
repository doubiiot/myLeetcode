class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right):
            pivot = nums[right]
            i = left - 1
            for j in range(left, right):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[right] = nums[right], nums[i+1]
            return (i + 1)

        def quick_sort(nums, left, right):
            if left < right:
                idx = partition(nums, left, right)
                partition(nums, left, idx-1)
                partition(nums, idx+1, right)

        quick_sort(nums, 0, len(nums)-1)
        return nums[-k]
#改进快排 排序完成后返回倒数第k个元素