class Solution:
    def numSquares(self, n: int) -> int:
        lst = [i ** 2 for i in range(1,int(math.sqrt(n))+1)]
        def func(n, count):
            if count == 1:
                return n in lst
            for var in lst:
                if func(n - var, count - 1):
                    return True
            return False

        for i in range(1, n+1):
            if func(n, i):
                return i
# O(n ^ (h/2)) O(n ^ 0.5)
# h为可能发生的最大递归次数
