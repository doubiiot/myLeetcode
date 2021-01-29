class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def max_heapify(arrs, start, end):
            left = 2 * start + 1
            right = 2 * start + 2
            max_pos = start
            if left <= end and arrs[left] > arrs[max_pos]:
                max_pos = left
            if right <= end and arrs[right] > arrs[max_pos]:
                max_pos = right
            if max_pos != start:
                arrs[max_pos], arrs[start] = arrs[start], arrs[max_pos]
                return max_heapify(arrs, max_pos, end)
            else:
                return arrs

        length = len(nums)
        end = length - 1
        for i in range(length//2 - 1, -1, -1):
            nums = max_heapify(nums, i, end)
        for i in range(length-1, length-k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            end -= 1
            nums = max_heapify(nums, 0, end)
        return nums[0]




