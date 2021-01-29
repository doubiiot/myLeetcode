class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        length = len(intervals)
        intervals.sort(key=lambda x: x[0])
        dp = [1] * length
        dp[0] = 1
        for i in range(1, length):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return length - max(dp)
#O(N^2) O(N)
#动态规划的思想，此题Python超时
