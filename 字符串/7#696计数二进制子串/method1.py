class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n, last, res = len(s), 0, 0
        cur = 0
        while cur < n:
            cur_num = 0
            c = s[cur]
            while cur < n and s[cur] == c:
                cur += 1
                cur_num += 1
            res += min(cur_num, last)
            last = cur_num
        return res
# O(N) O(1)
# 改进代码
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        p1, p2, res = 0, 1, 0
        for i in range(1, n):
            if s[i] == s[i-1]: p2 += 1
            else:
                res += min(p1, p2)
                p1 = p2
                p2 = 1
        res += min(p1, p2)
        return res

