t = int(input())

if t % 10 != 0:
    print(-1)
else:
    A, B, C = 0, 0, 0
    A = t//300
    B = (t%300)//60
    C = (t%300)%60 // 10
    print(A, B, C)

#######################

t = int(input())
a, b, c = 300, 60, 10
A, B, C = 0, 0, 0
if t % c != 0:
    print(-1)
else:
    if t >= a:
        A += t//a
        t %= a
    if t >= b:
        B += t//b
        t %= b
    if t >= c:
        C += t//c
        t %= c
    print(A, B, C)
