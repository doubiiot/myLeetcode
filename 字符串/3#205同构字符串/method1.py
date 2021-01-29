class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def func(s, t):
            dic = {}
            for i in range(len(s)):
                # if s[i] not in dic:
                if dic.get(s[i], 0) == 0:
                    dic[s[i]] = t[i]
                elif dic.get(s[i]) != t[i]:
                    return False
            return True
        return func(s, t) and func(t, s)
# O(N) O(n)
