n, m = map(int, input().split())

if n == 1:
    result = 1
elif n == 2:
    result = min(4, (m-1)//2 +1)
elif m < 7:
    result = min(4, m)
else:
    result = m - 2
print(result)