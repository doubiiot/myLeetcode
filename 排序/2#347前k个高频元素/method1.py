class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # down
        def sift_down(arrs, start, end):
            left = 2 * start + 1
            right = 2 * start + 2
            min_pos = start
            if left <= end and arrs[left][1] < arrs[min_pos][1]: min_pos = left
            if right <= end and arrs[right][1] < arrs[min_pos][1]: min_pos = right
            arrs[min_pos], arrs[start] = arrs[start], arrs[min_pos]
            return arrs if min_pos == start else sift_down(arrs, min_pos, end)
        def sift_up(arrs, start, end):
            #注意父节点的计算！！！
            parent = (end - 1) // 2
            if parent >= start and arrs[end][1] < arrs[parent][1]:
                arrs[end], arrs[parent] = arrs[parent], arrs[end]
                return sift_up(arrs, start, parent)
            else:
                return arrs


        arrs = collections.Counter(nums)
        arrs = list(arrs.items())
        heap = []
        #create heap sift_up
        for i in range(k):
            heap.append(arrs[i])
            heap = sift_up(heap, 0, i)
        #insert sift_down
        for j in range(k, len(arrs)):
            if arrs[j][1] > heap[0][1]:
                heap[0] = arrs[j]
                heap = sift_down(heap, 0, k-1)
        rslt = []
        for key in heap:
            rslt.append(key[0])
        return rslt

