class Solution:
    def isValid(self, s: str) -> bool:
        #11.20
        def ispair(c1, c2):
            if (c1 == '}' and c2 == '{') or (c1 == ']' and c2 == '[') or (c1 == ')' and c2 == '('):
                return True
            else:
                return False
        stk = []
        for c in s:
            if not stk or not ispair(c, stk[-1]):
                stk.append(c)
            else:
                stk.pop()
        return False if stk else True
