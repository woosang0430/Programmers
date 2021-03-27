s = '00011001'

compare = [0, 0]

if s[0] == '1':
    compare[0] += 1
else:
    compare[1] += 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        if s[i] == '1':
            compare[0] += 1
        else:
            compare[1] += 1

print(min(compare))