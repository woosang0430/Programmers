n = int(input())

def fac(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

tmp = str(fac(n))
cnt = 0
for i in range(1, len(tmp)+1):
    if tmp[-i] == '0':
        cnt += 1
    else:
        break
print(cnt)
