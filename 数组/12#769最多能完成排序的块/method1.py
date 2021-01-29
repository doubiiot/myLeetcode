class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        l = r = 0
        res = 1
        while r < len(arr)-1:
            if max(arr[l:r+1]) < min(arr[r+1:]):
                l = r + 1
                r = r + 1
                res += 1
            else:
                r += 1
        return res
#O(N) O(1)
