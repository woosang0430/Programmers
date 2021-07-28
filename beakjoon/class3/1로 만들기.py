from collections import deque

n = int(input())
dq = deque([[n, 0]])
visited = set()

def solution(num, cnt, n):
    if num%n == 0 and num//n not in visited:
        dq.append([num//n, cnt+1])
        visited.add(num//n)

while dq:
    num, cnt = dq.popleft()
    if num == 1:
        break
    solution(num, cnt, 3)
    solution(num, cnt, 2)
    if num-1 not in visited:
        dq.append([num-1, cnt+1])
        visited.add(num-1)
print(cnt)

############################################3

def dq(n):
    if n in memo:
        return memo[n]
    
    m = 1 + min(dq(n//2)+ n%2, dq(n//3)+ n%3)
    memo[n] = m
    return m

memo = {1:0, 2:1}
n = int(input())

print(dq(n))