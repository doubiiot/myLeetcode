class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import random
        def partition(left, right):
            nonlocal nums
            i = left - 1
            pivot = nums[right]
            for j in range(left, right):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[right] = nums[right], nums[i+1]
            return i+1
        def quick_sort(left, right):
            nonlocal nums
            if left < right:
                cur = random.randint(left, right)
                nums[cur], nums[right] = nums[right], nums[cur]
                idx = partition(left, right)
                quick_sort(left, idx-1)
                quick_sort(idx+1, right)

        quick_sort(0, len(nums)-1)
