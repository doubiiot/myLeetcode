class Solution:
    def isVowels(self, c):
        if c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
            return True
        else:
            return False
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s)-1
        while start < end:
            if self.isVowels(s[start]) and self.isVowels(s[end]):
                s[start],s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif self.isVowels(s[start]):
                end -= 1
            elif self.isVowels(s[end]):
                start += 1
            else:
                start += 1
                end -= 1
        return ''.join(s)