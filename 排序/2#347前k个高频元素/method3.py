class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items() :
            # 如果堆满了（k个元素）
            if len(heap) == k :
                # 弹出最小频率的元组
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else :
                hq.heappush(heap, (freq, num))
        while heap :
            res.append(hq.heappop(heap)[1])
        return res
