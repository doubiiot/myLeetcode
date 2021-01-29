s = "I am a student"
def reverse_str(s):
    return s[::-1]
lst = s.split()
print(lst)
s = reverse_str(lst)
print(s)
print(' '.join(s))
