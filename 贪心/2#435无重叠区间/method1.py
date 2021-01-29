class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x : x[0])
        num = 0
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            cur_l, cur_r = intervals[i][0], intervals[i][1]
            if cur_l >= start and cur_r <= end:
                start, end = cur_l, cur_r
                num += 1
            elif cur_l >= start and cur_l < end and cur_r > end:
                num += 1
            elif cur_l >= end:
                 start, end = cur_l, cur_r
        return num
