# 11 x 11 배열의 맵
# 한가운데의 캐릭터 위치 
# 처음 걸어본 길의 길이를 반환
# 맵을 벗어나거나 걸었던 길은 제외한다.

# 방향 지정 함수정의
def direct_func(direction):
    if direction == 'U':
        ret = 0
    elif direction == 'L':
        ret = 1
    elif direction == 'D':
        ret = 2
    else:
        ret = 3
    return ret

# dirs = "ULURRDLLU"
dirs = "LULLLLLLU"

# 맵 생성
map_arr = [[0] * 11 for _ in range(11)]
# 초기 캐릭터 생성
map_arr[5][5] = 1
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
y, x = 5, 5

overlap = 1

for i in dirs:
    dirs_idx = direct_func(i)
    ny = y + dy[dirs_idx]
    nx = x + dx[dirs_idx]

    # 맵을 벗어나면 pass~
    if ny == -1 or nx == -1 or ny == 11 or nx == 11:
        continue
    elif overlap == 0:
        # 중복되는 값이 있으면 한번만 +1해주기
        answer += 1

    # 안가봤으면 영역표시 남기고 가자
    if map_arr[ny][nx] == 0:
        map_arr[ny][nx] = 1
        answer += 1
        # 안가본 곳에 가면 overlap은 항시 1로 대기
        overlap = 1
    # 가봤으면 그냥 이동만
    else:
        # 가본 곳이면 2번째 부터 체크해주기 위해 -1씩
        overlap -= 1
    y, x = ny, nx

print(answer)

# ###################################
"""
위의 코드를 짜면서 굳이 맵을 짤 필요 없다는 것을 느낌
맵 없이 좌표만으로
"""

# dirs = "ULURRDLLU"
dirs = "LULLLLLLU"

answer = 0
overlap = 1
node = []

y, x = 0, 0
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

for i in dirs:
    idx = direct_func(i)
    ny = y + dy[idx]
    nx = x + dx[idx]

    if ny == -6 or nx == -6 or ny == 6 or nx == 6:
        continue
    elif overlap == 0:
        answer += 1
    
    if [ny, nx] not in node:
        node.append([ny, nx])
        answer += 1
        overlap = 1
    else:
        overlap -= 1
    y, x = ny, nx

print(answer)
"""
[실패 이유]
중복된 값을 정확하게 처리하지 못하였다....

[문제 해결법]
이동한 노드 두개를 리스트로 묶어 저장 
    - 이때 set을 이용하여 중복이 되지 않게 한다.
    - 리스트끼리의 묶음이므로 정렬이 중요 set에 add하기 전에 정렬을 하고 넣자
"""