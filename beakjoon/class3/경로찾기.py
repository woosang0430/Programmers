from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
location_info = {i:set() for i in range(N)}
for y in range(N):
    temp_list = [*map(int, input().split())]
    location_info[y].update([i for i, v in enumerate(temp_list) if v == 1])

# answer = []
for i in range(N):
    visited = [0] * N
    dq = deque([i])
    while dq:
        node = dq.popleft()
        for j in location_info[node]:
            if visited[j] == 0:
                visited[j] = 1
                dq.append(j)
    # answer.append(visited)
    print(*visited)
# print(answer)