class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def func(mid, n):
            cur = n - 1
            num = 0
            for i in range(n):
                while cur >= 0 and matrix[cur][i] > mid:
                    cur -= 1
                num += (cur + 1)
            return num >= k

        l, r = matrix[0][0], matrix[-1][-1]
        n = len(matrix)
        while l < r:
            mid = l + (r - l) // 2
            if func(mid, n):
                r = mid
            else:
                l = mid + 1
        return l
# O(nlog(r-l)) O(1)
