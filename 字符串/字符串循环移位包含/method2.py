s1 = 'AABCD'
s2 = 'CDAA'
n = len(s1)
cur = 0
while cur < n:
    if s2 in s1:
        print('true')
    s1 = s1[-1] + s1[0:-1]
    cur += 1
print('false')
# O(N)
