class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(i, start, end, flag):
            while start <= end:
                mid = start + (end - start) // 2
                #行查找
                if flag:
                    if matrix[i][mid] > target:
                        end = mid - 1
                    elif matrix[i][mid] < target:
                        start = start + 1
                    else:
                        return True
                #列查找
                else:
                    if matrix[mid][i] > target:
                        end = mid - 1
                    elif matrix[mid][i] < target:
                        start = start + 1
                    else:
                        return True
            return False

        row = len(matrix)
        col = len(matrix[0])
        for i in range(min(row, col)):
            #查找行
            herizion_fount = binary_search(i, i, col-1, 1)
            #查找列
            vertical_found = binary_search(i, i, row-1, 0)
            if vertical_found or herizion_fount:
                return True
        return False
# O(log(n!) O(1)
