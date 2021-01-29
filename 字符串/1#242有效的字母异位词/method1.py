class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s, dic_t = {}, {}
        for val in s: dic_s[val] = dic_s.get(val, 0) + 1
        for val in t: dic_t[val] = dic_t.get(val, 0) + 1
        if len(dic_s) != len(dic_t):
            return False
        else:
            for k in dic_s:
                if k not in dic_t or dic_s[k] != dic_t[k]:
                    return False
            return True
