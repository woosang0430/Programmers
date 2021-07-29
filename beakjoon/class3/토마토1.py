from collections import deque
import sys
input = sys.stdin.readline

def bfs(location_info):
    dy = [-1, 0, 1, 0, 0, 0]
    dx = [0, -1, 0, 1, 0, 0]
    dq = deque(location_info)
    tmp = []
    spread = 0
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny in range(Y) and nx in range(X) and tomato_box[ny][nx] == 0:
                tomato_box[ny][nx] = 1
                spread += 1
                tmp.append((ny, nx))
    return spread, tmp

X, Y = map(int, input().split())

zero_cnt = 0
location_info = []
tomato_box = []
for y in range(Y):
    temp = list(map(int, input().split()))
    location_info.extend([(y, x) for x, v in enumerate(temp) if v == 1])
    zero_cnt += temp.count(0)
    tomato_box.append(temp)

answer = 0
while location_info:
    spread, location_info = bfs(location_info)
    if spread:
        zero_cnt -= spread
        answer += 1

print(-1 if zero_cnt else answer)