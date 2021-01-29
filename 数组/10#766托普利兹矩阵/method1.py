class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m-1):
            if matrix[i][0:n-1] != matrix[i+1][1:n]:
                return False
        return True
# O(M*N) O(1)
