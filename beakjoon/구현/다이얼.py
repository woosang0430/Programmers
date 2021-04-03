alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num_alpha = dict()
cnt = 2
for i in alpha:
    if i in ['D', 'G', 'J', 'M', 'P', 'T', 'W']:
        cnt += 1
    num_alpha[i] = cnt

s = input()
result = len(s)
for i in s:
    result += num_alpha[i]

print(result)