class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        r, c = row-1, 0
        while r >= 0 and c < col:
            if matrix[r][c] == target: return True
            elif matrix[r][c] > target: r -= 1
            else: c += 1
        return False
# O(M+N) O(1) best
