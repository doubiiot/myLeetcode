s = "abcd123"
k = 3
def reverse_str(s):
    return s[::-1]
n = len(s)
mid_str = reverse_str(s[0:-k]) + reverse_str(s[-k:])
print(reverse_str(mid_str))
