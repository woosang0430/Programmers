from collections import deque
places = ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]

people_loc = []
for y in range(5):
    places[y] = list(places[y])
    for x in range(5):
        if places[y][x] == 'P':
            people_loc.append((y, x))

def check_distance(people_loc):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    for loc in people_loc:
        dq = deque([loc])
        cnt = 0
        while dq and cnt != 2:
            y, x = dq.popleft()
            places[y][x] = 'p'
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny in range(5) and nx in range(5):
                    if places[ny][nx] == 'O':
                        dq.append((ny, nx))
                    elif places[ny][nx] == 'P':
                        return 0
            cnt += 1
    return 1

print(check_distance(people_loc))
###########################################################################
from collections import deque
def solution(places):
    def check_around(loc):
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        cnt = 0
        y, x = loc
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(5) and nx in range(5):
                if place[ny][nx] == 'O':
                    cnt +=1
        if cnt < 2:
            return True
        return False

    def check_distance(people_loc):
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        for loc in people_loc:
            dq = deque([loc])
            cnt = 0
            limit = 3
            if check_around(loc):
                limit = 2
            while dq and cnt != limit:
                y, x = dq.popleft()
                place[y][x] = 'A'
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny in range(5) and nx in range(5):
                        if place[ny][nx] == 'O':
                            dq.append((ny, nx))
                        elif place[ny][nx] == 'P':
                            return 0
                cnt += 1
        return 1

    answer = []
    for place in places:
        people_loc = []
        for y in range(5):
            place[y] = list(place[y])
            for x in range(5):
                if place[y][x] == 'P':
                    people_loc.append((y, x))
        answer.append(check_distance(people_loc))
    return answer
    
s = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(s))