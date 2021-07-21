N, M = map(int, input().split())
N, M = max(N, M), min(N, M)

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

answer = gcd(N, M)
print(answer, N*M//answer, sep='\n')