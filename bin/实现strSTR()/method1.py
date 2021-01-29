class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_next(S):
            nxt = [-1]
            x, now = 0, -1
            while x < len(S):
                if now == -1 or S[x] == S[now]:
                    x += 1
                    now += 1
                    nxt.append(now)
                elif now:
                    now = nxt[now]
                else:
                    nxt.append(0)
                    x += 1
            return nxt[:-1]
        def KMP():
            nxt = get_next(needle)
            i, j, var = 0, 0, 0
            while j < len(needle):
                if i >= len(haystack):
                    return -1
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    i -= nxt[j]
                    j = 0
                    var = i
            return var
        return KMP()
