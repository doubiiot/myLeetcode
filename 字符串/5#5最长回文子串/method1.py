class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l_m, r_m, max_ = 0, 0, 0
        for i in range(2*n-1):
            l = i // 2
            r = l + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > max_:
                max_ = r - l - 1
                l_m = l
                r_m = r
        return s[l_m + 1 : r_m]
# 中心扩展方法
# 也可以使用动态规划（空间复杂度高，可能可以优化为O(N) ）
# 最优算法 manacher算法 O(N) O(N) （未实现）
