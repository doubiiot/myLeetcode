# 时间复杂度：O(nlog(n-k))；当k和n相当时，用此法
# 从m个元素中，通过堆选出最大的k个数；m-k 大小的堆 -- 大根堆
# 堆满后，若新加的数小于堆首数，堆首元素加入结果，否则新加的数加入结果 -- 选了k次最大的
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        res = []

        heap = []
        lookup = Counter(nums)
        n = len(lookup)
        for num, freq in lookup.items() :
            if len(heap) == n-k :
                if heap and -heap[0][0] > freq :
                    res.append(hq.heapreplace(heap, (-freq, num))[1])
                else : res.append(num)
            else :
                hq.heappush(heap, (-freq, num))
        return res
