from collections import deque
from typing import Dict, List

def check(shark_size: int, fish_info: Dict[int, int]) -> bool:
    # 엄마 상어를 부를 것인지 확인하는 함수
    for fish_size, cnt in fish_info.items():
        if cnt != 0 and fish_size < shark_size:
            return True
    return False

def search_around(shark_info: List[int]) -> List[int]:
    shark_loc = tuple(shark_info[:2])
    visited = {shark_loc}
    dq = deque([shark_info[:3]+[0]])
    _eat_info = []
    temp = []
    while dq:
        y, x, size, _time = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(N) and nx in range(N) and (ny, nx) not in visited:
                if size >= sea_map[ny][nx]:
                    visited.add((ny, nx))
                    if size == sea_map[ny][nx] or sea_map[ny][nx] == 0:
                        temp.append((ny, nx, size, _time+1)) # y, x, shark_size, time
                    else:
                        _eat_info.append((ny, nx, sea_map[ny][nx], _time+1)) # y, x, fish_size, time
        if len(dq) == 0:
            if len(_eat_info) == 0:
                dq.extend(temp)
                temp.clear()
            else:
                _eat_info.sort(key=lambda x: (x[0], x[1]))
                return _eat_info[0]

N = int(input())
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
sea_map = []
fish_info = {i:0 for i in range(1, 7)}
shark_info = [0, 0, 2, 0] # y, x, size, eat
for i in range(N):
    tmp = list(map(int, input().split()))
    sea_map.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] not in [0, 9]:
            fish_info[tmp[j]] += 1
        elif tmp[j] == 9:
            shark_info[:2] = i, j
            sea_map[i][j] = 0

time = 0
while True:
    if check(shark_info[2], fish_info) == False:
        break
    eat_info = search_around(shark_info)
    if not eat_info:
        break
    y, x = eat_info[:2]
    sea_map[y][x] = 0 # clean fish location
    shark_info[:2] = y, x # relocation
    shark_info[3] += 1 # eating check
    fish_info[eat_info[2]] -= 1 # fish count minus
    time += eat_info[3] # move time plus
    if shark_info[2] == shark_info[3]: # size up
        shark_info[2] += 1
        shark_info[3] = 0
print(time)