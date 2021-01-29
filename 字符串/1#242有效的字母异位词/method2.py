class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        lst = [0] * 26
        for c in s:
            lst[ord(c) - ord('a')] += 1
        for c in t:
            lst[ord(c) - ord('a')] -= 1
            if lst[ord(c) - ord('a')] < 0:
                return False
        return True

