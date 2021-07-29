from collections import deque

N = int(input())
map_arr = [list(input()) for _ in range(N)]

def bfs(y, x, cnt):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    dq = deque([(y, x)])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(N) and nx in range(N) and map_arr[ny][nx] == '1':
                map_arr[ny][nx] = '0'
                dq.append((ny, nx))
                cnt += 1
    return cnt

answer = []
for y in range(N):
    for x in range(N):
        if map_arr[y][x] == '1':
            map_arr[y][x] = '0'
            result = bfs(y, x, 1)
            answer.append(result)

print(len(answer))
for i in sorted(answer):
    print(i)