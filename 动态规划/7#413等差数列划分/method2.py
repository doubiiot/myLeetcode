class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 2:
            return 0
        dp = [0 for _ in range(n)]
        for i in range(2,n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1 + dp[i-1]
        return sum(dp)
#O(n) O(1)
