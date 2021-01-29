class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x : x[0])
        num = 0
        start, end = points[0]
        for i in range(1, len(points)):
            cur_l, cur_r = points[i][0], points[i][1]
            if cur_l >= start and cur_r <= end:
                start, end = cur_l, cur_r
                num += 1
            elif (cur_l >= start and cur_l <= end) and (cur_r >= end):
                num += 1
            elif cur_l > end:
                 start, end = cur_l, cur_r
        return len(points) - num
