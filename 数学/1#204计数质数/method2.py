class Solution:
    def countPrimes(self, n: int) -> int:
        mark = [1 for i in range(n)]
        prime = []
        num = 0
        for i in range(2, n):
            if mark[i]:
                prime.append(i)
                num += 1
            for j in range(num):
                if i * prime[j] >= n:
                    break
                mark[i * prime[j]] = 0
                if i % prime[j] == 0:
                    break
        return num
#O(n) O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        mark = [1 for i in range(n)]
        prime = []
        for i in range(2, n):
            if mark[i]:
                prime.append(i)
            for j in range(len(prime)):
                if i * prime[j] >= n:
                    break
                mark[i * prime[j]] = 0
                if i % prime[j] == 0:
                    break
        return len(prime)

