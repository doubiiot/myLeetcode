class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arrs = collections.Counter(nums)
        return heapq.nlargest(k, arrs.keys(), key=arrs.get)

