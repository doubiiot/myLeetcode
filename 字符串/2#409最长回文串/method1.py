class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        num, flag = 0, 0
        for v in dic.values():
            num += v // 2
            if v % 2:
                flag = 1
        return 2 * num + flag
