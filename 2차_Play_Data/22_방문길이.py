# 방향 함수 정의
def direct_func(dir):
    if dir == "U":
        ret = 0
    elif dir == "L":
        ret = 1
    elif dir == "D":
        ret = 2
    else:
        ret = 3
    return ret

def solution(dirs):
    y, x = 0, 0
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    # 중복값을 제거해 주기 위해 set ㄱㄱ
    nodes = set()

    for i in dirs:
        idx = direct_func(i)
        ny = y + dy[idx]
        nx = x + dx[idx]

        # 맵 벗어나면 pass~
        if ny == -6 or ny == 6 or nx == -6 or nx == 6:
            continue
        # 리스트 안의 값들을 정렬해줘야 같은 값인지 아닌지 식별 가능
        node = tuple(sorted([(ny, nx), (y, x)]))
        nodes.add(node)
        y, x = ny, nx
    return len(nodes)

print(solution('LULLLLLLU'))

# 다른 사람 코드
def solution(dirs):
    answer = 0
    dx = {"U" : 0, "D" : 0, "R" : 1, "L" : -1}
    dy = {"U" : -1, "D" : 1, "R" : 0, "L" : 0}

    # prev = (0, 0)
    _x, _y = 0, 0
    footprint = set()

    for d in dirs:
        # _x, _y = prev
        x = _x + dx[d]
        y = _y + dy[d]

        if -5 <= x <= 5 and -5 <= y <= 5:
            foot = tuple(sorted([(_x, _y), (x, y)]))
            footprint.add(foot)
            # prev = (x, y)
            _x, _y = x, y

    answer = len(footprint)

    return answer

print(solution("LULLLLLLU"))

## 최종 나의 코드
def solution(dirs):
    nodes = set()
    y, x = 0, 0
    dy = {"U":-1, "L":0, "D":1, "R":0}
    dx = {"U":0, "L":-1, "D":0, "R":1}
    
    for i in dirs:
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny == -6 or ny == 6 or nx == -6 or nx == 6:
            continue
        
        node = tuple(sorted([(ny, nx), (y, x)]))
        nodes.add(node)
        y, x = ny, nx
    
    return(len(nodes))