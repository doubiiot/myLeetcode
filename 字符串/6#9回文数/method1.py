class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x != 0 and x % 10 == 0:
            return False
        cur  = 0
        while x > cur:
            num = x % 10
            cur = cur * 10 + num
            x = x // 10
        if x == cur or x == cur // 10:
            return True
        else:
            return False
# O(logN) O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0 or not x % 10: return False
        cur  = 0
        while x > cur:
            cur = cur * 10 + x % 10
            x = x // 10
        return x == cur or x == cur // 10

