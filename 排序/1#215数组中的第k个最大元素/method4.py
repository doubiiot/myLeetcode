class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def build_maxheap(nums, start, end):
            max_pos = start
            while True:
                left = 2 * start + 1
                right = 2 * start + 2
                if left <= end and nums[left] > nums[start]:
                    max_pos = left
                if right <= end and nums[right] > nums[max_pos]:
                    max_pos = right
                if max_pos == start:
                    break
                nums[max_pos], nums[start] = nums[start], nums[max_pos]
                start = max_pos
            return nums
        length = len(nums)
        for i in range(length//2 - 1, -1, -1):
            nums = build_maxheap(nums, i, length-1)

        flag = 1
        for j in range(k-1):
            nums[0], nums[-1] = nums[-1], nums[0]
            nums = nums[0:-1]
            nums = build_maxheap(nums, 0, length-1-flag)
            flag += 1
        return nums[0]

