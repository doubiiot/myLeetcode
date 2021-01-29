class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s: return True
        dic = {}
        for i in range(len(s)):
            # if s[i] not in dic:
            if dic.get(s[i], 0) == 0:
                if t[i] in dic.values():
                    return False
                dic[s[i]] = t[i]
            elif dic[s[i]] != t[i]:
                return False
        return True
# 感觉时间复杂度是O(N^2)，主要看t[i] in dic.values()操作咋样
