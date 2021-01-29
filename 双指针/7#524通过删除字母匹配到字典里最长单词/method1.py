class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        dic, rslt, max_ = {}, [], -1
        s += '0'
        for word in d:
            word += '0'
            p1, p2 = 0, 0
            while s[p1] != '0' and word[p2] != '0':
                if s[p1] == word[p2]:
                    p2 += 1
                p1 += 1
            if word[p2] == '0':
                max_ = p2 if p2 > max_ else max_
                dic[word[:-1]] = p2
        for k,v in dic.items():
            if v == max_:
                rslt.append(k)
        if not rslt: return ""
        rslt.sort()
        return rslt[0]

# O(N^2) O(N)