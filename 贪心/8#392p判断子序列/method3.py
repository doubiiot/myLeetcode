# 后续挑战 :
# 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，
# 你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        # create a matrix shape of m+1 * 26
        f = [[0] * 26 for i in range(m)]
        f.append([m]*26)
        # construct matrix
        for i in range(m-1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i+1][j]

        var = 0
        for j in s:
            if f[var][ord(j) - ord('a')] == m:
                return False
            var = f[var][ord(j) - ord('a')] + 1
        return True
# Time O(m * |N| + n)
# Space O(m * |N|) N为字符集的长度
