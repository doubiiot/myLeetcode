class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(2*n-1):
            l_i = i // 2
            r_i = l_i + i % 2
            while l_i >= 0 and r_i < n:
                if s[l_i] == s[r_i]:
                    res += 1
                    l_i -= 1
                    r_i += 1
                else:
                    break
        return res
#O(N^2) O(1)
#代码优化：
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(2*n-1):
            l_i = i // 2
            r_i = l_i + i % 2
            while l_i >= 0 and r_i < n and s[l_i] == s[r_i]:
                res += 1
                l_i -= 1
                r_i += 1
        return res



