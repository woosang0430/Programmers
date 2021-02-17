n = int(input())

cnt = 0
while n:
    if n%2 == 1 or n%2 == 2:
        cnt+=1
    n //=2
print(cnt)

# 다른 사람 코드
def solution(n):
    return bin(n).count('1')