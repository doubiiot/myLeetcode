class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return isPalindrome(low + 1, high) or isPalindrome(low, high - 1)
        return True

# O(N) O(1)