class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        mat = [[1, 1], [1, 0]]
        def mat_multi(mat1, mat2):
            res = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    res[i][j] = mat1[i][0] * mat2[0][j] + mat1[i][1] * mat2[1][j]
            return res
        res = mat
        for i in range(n-1):
            res = mat_multi(mat, res)
        res = res[1][0] + res[1][1]
        return res
#O(logn) O(1)
