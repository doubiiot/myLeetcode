class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        counter = collections.Counter(s)
        num = 0
        for v in counter.values():
            num += v // 2 * 2
            if num % 2 == 0 and v % 2:
                num += 1
        return num
# O(N) O(S)
