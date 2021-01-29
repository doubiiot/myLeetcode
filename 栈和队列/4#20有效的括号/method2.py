class Solution:
    def isValid(self, s: str) -> bool:
        #11.20
        pair = {
            '}':'{',
            ']':'[',
            ')':'(',
        }
        stk = []
        for c in s:
            if c in pair:
                if not stk or stk[-1] != pair[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return not stk
