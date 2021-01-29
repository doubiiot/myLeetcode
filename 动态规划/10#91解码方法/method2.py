class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [1] * (n+1)
        pre_s, pre_q = 1, 1
        cur = 1
        for i in range(2, n+1):
            if s[i-1] == '0' and s[i-2] not in ['1', '2']:
                return 0
            if s[i-2:i] in ['10', '20']:
                cur = pre_s
            elif '10' < s[i-2:i] <= '26':
                cur = pre_s + pre_q
            else:
                dp[i] = pre_q
            pre_s = pre_q
            pre_q = cur
        return cur
# O(n) O(1)
