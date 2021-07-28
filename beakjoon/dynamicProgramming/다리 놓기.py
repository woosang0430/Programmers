from math import factorial as fac

for  _ in range(int(input())):
    n, m = map(int, input().split())
    ret = fac(m) // fac(m-n) // fac(n)
    print(ret)

########################################

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = factorial(m) // (factorial(n) * factorial(m-n))
    print(answer)
