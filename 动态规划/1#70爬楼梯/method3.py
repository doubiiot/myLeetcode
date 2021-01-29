class Solution:
    def climbStairs(self, n: int) -> int:
        x = pow(5, 0.5)
        return int((pow((1+x)/2, n+1) - pow((1-x)/2, n+1)) / x)
#O(logn) O(1)
