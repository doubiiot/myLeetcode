class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        str_new = '!#'
        for i in range(n):
            str_new += s[i]
            str_new += '#'
        str_new += '?'
        n = 2 * n + 2
        f = [0 for i in range(n)]
        res, i_m, r_m = 0, 0, 0
        for i in range(1, n):
            j = 2 * i_m - i
            f[i] = min(f[j], r_m - i + 1) if i <= r_m else 1
            while str_new[i + f[i]] == str_new[i - f[i]]:
                f[i] += 1
            if f[i] + i - 1 > r_m:
                i_m = i
                r_m = f[i] + i - 1
            res += f[i] // 2
        return res
# O(N) O(N)
#Manacher算法



