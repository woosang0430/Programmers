N = int(input())

for _ in range(N):
    i = int(input())
    a, b = 1, 0
    if i <= 0:
        print(a, b)
    else:
        for _ in range(i-1):
            c = a + b
            a, b = c, a
        print(b, a)