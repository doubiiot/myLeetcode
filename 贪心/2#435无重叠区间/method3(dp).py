class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        length = len(intervals)
        intervals.sort(key=lambda x: x[0])
        dp = [1] * length
        dp[0] = 1
        for i in range(1, length):
            for j in range(i-1, -1, -1):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
        return length - max(dp)
#方法2的改进 不超时
