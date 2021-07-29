from collections import deque
import sys
input = sys.stdin.readline

def bfs(location_info, box):
    dh = [0, 0, 0, 0, -1, 1]
    dy = [-1, 0, 1, 0, 0, 0]
    dx = [0, -1, 0, 1, 0, 0]
    dq = deque(location_info)
    tmp = []
    spread = 0
    while dq:
        h, y, x = dq.popleft()
        for i in range(6):
            nh, ny, nx = h+dh[i], y+dy[i], x+dx[i]
            if nh in range(H) and ny in range(Y) and nx in range(X) and box[nh][ny][nx] == 0:
                box[nh][ny][nx] = 1
                spread += 1
                tmp.append((nh, ny, nx))
    return spread, tmp

def solution(X, Y, H):
    box = []
    zero_cnt = 0
    location_info = []
    for i in range(H):
        tomato_box = []
        for j in range(Y):
            temp = list(map(int, input().split()))
            location_info.extend([(i, j, k) for k, v in enumerate(temp) if v == 1])
            zero_cnt += temp.count(0)
            tomato_box.append(temp)
        box.append(tomato_box)

    answer = 0
    while location_info:
        spread, location_info = bfs(location_info, box)
        if spread:
            zero_cnt -= spread
            answer += 1
            
    return -1 if zero_cnt else answer

X, Y, H = map(int, input().split())
print(solution(X, Y, H))