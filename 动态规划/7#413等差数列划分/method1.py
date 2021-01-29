class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length = len(A)
        res = 0
        if length < 3:
            return 0
        for pre in range(length-2):
            var = A[pre+1] - A[pre]
            for rear in range(pre+2, length):
                if A[rear] - A[rear-1] == var:
                    res += 1
                else:
                    break
        return res
