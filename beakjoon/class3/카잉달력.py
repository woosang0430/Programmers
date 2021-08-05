import sys
input = sys.stdin.readline

def gcd(x, y): # 최대 공약수
    x, y = max(x, y), min(x, y)
    while y:
        x, y = y, x%y
    return x

N = int(input())
for _ in range(N):
    m, n, x, y = map(int, input().split())
    limit = m*n//gcd(m, n) # 최소 공배수 ==> 마지막 해(M, N)
    answer = -1
    while x < limit:
        if x%n == y%n:
            answer = x
            break
        x += m
    print(answer)