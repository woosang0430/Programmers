from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
relationship = {i:set() for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    relationship[a].add(b)
    relationship[b].add(a)

result = []
for current in range(1, n+1):
    visited = [False] * (n+1)
    cost = [0] * (n+1)
    visited[current] = True
    dq = deque([current])
    while dq:
        curr = dq.popleft()
        for i in relationship[curr]:
            if visited[i] == False:
                visited[i] = True
                cost[i] += 1 + cost[curr]
                dq.append(i)
    result.append([current, sum(cost)])
result.sort(key=lambda x: (x[1], x[0]))

print(result[0][0])
