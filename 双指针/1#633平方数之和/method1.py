class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c ** 0.5)
        while i <= j:
            num = i * i + j * j
            if num > c: j -= 1
            elif num < c: i += 1
            else: return True
        return False
# 双指针 O(sqrt(n)) O(1)
