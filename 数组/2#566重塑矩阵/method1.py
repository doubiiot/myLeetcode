class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0]) if row else 0
        if row * col != r * c:
            return nums
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                loc = i * c + j
                m = loc // col
                n = loc - m * col
                res[i][j] = nums[m][n]
        return res
