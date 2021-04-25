for _ in range(int(input())):
    width, height, len_cabbage = map(int, input().split())
    cabbage_info = [list(map(int, input().split())) for _ in range(len_cabbage)]
    cnt = 0
    while cabbage_info:
        stack = [cabbage_info.pop(0)]
        while stack:
            x, y = stack.pop()
            NEWS = [[x, y-1], [x+1, y], [x, y+1], [x-1, y]]
            for direction in NEWS:
                if direction in cabbage_info:
                    stack.append(direction)
                    cabbage_info.remove(direction)
        cnt += 1
    print(cnt)

######################################################
def dfs(maps, x, y):
    maps[y][x] = 0
    if y-1 >= 0 and maps[y-1][x] == 1:
        dfs(maps, x, y-1)
    if y+1 < height and maps[y+1][x] == 1:
        dfs(maps, x, y+1)
    if x-1 >= 0 and maps[y][x-1] == 1:
        dfs(maps, x-1, y)
    if x+1 < width and maps[y][x+1] == 1:
        dfs(maps, x+1, y)

for _ in range(int(input())):
    width, height, len_cabbage = map(int, input().split())
    maps = [[0]*width for _ in range(height)]
    cnt = 0

    for _ in range(len_cabbage):
        x, y = map(int, input().split())
        maps[y][x] = 1
    
    for y in range(height):
        for x in range(width):
            if maps[y][x] == 1: 
                dfs(maps, x, y)
                cnt += 1
    print(cnt)

###########################################################
import sys
sys.setrecursionlimit(10 ** 6)
# 파이썬 재귀에서는 꼭이거 넣어주자...
input = sys.stdin.readline

def dfs1(maps, x, y):
    if x <= -1 or y <= -1 or x >= width or y >= height:
        return False
    if maps[y][x] == 1:
        maps[y][x] = 0
        dfs1(maps, x-1, y)
        dfs1(maps, x+1, y)
        dfs1(maps, x, y-1)
        dfs1(maps, x, y+1)
        return True
    return False
    

for _ in range(int(input())):
    width, height, len_cabbage = map(int, input().split())
    maps = [[0]*width for _ in range(height)]

    for _ in range(len_cabbage):
        x, y = map(int, input().split())
        maps[y][x] = 1
    
    cnt = 0
    for y in range(height):
        for x in range(width):
            if dfs1(maps, x, y):
                cnt += 1
    print(cnt)