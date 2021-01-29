class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1:
            return 1
        path = deque()
        path.append([0,0])
        res = 1
        while path:
            for i in range(len(path)):
                x, y = path.popleft()
                for cur_x, cur_y in [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]:
                    if cur_x == n-1 and cur_y == n-1:
                        return res+1
                    if 0<=cur_x<n and 0<=cur_y<n and grid[cur_x][cur_y] == 0:
                        grid[cur_x][cur_y] = 1
                        path.append([cur_x,cur_y])
            #下一层 深度加一
            res += 1
        return -1

