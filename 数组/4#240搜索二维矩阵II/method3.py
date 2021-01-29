class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_target(left, right, up, down):

            if left > right or up > down:
                return False
            if target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2
            cur = up
            while cur <= down and matrix[cur][mid] <= target:
                if matrix[cur][mid] == target:
                    return True
                cur += 1
            return search_target(left, mid-1, cur, down) or search_target(mid+1, right, up, cur-1)

        return search_target(0, len(matrix[0])-1, 0, len(matrix)-1)
    # O(nlogn) 可以通过二分搜索进一步优化到O(logn)
    # O(1)
