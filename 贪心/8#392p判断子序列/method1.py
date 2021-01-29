class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t: return True
        cur = 0
        ls = len(s)
        for i in t:
            if cur < ls and s[cur] == i:
                cur += 1
            if cur == ls:
                return True
        return False
#O(N) O(1)
