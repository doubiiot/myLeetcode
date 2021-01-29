class Solution:
    def countPrimes(self, n: int) -> int:
        mark = [1 for i in range(n)]
        res = 0
        for i in range(2, n):
            if mark[i]:
                res += 1
                for j in range(i*i,n,i):
                    mark[j] = 0
        return res
# O(nlogn) O(n)
