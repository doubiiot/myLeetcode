class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res, tmp = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                tmp += 1
                res = tmp + res
            else:
                tmp = 0
        return res
#O(n) O(1)
