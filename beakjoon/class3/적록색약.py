from collections import deque
import sys
input = sys.stdin.readline

def solution(y, x, visited, board):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    dq = deque([(y, x)])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(N) and nx in range(N) and \
                not visited[ny][nx] and board[ny][nx] == board[y][x]:
                visited[ny][nx] = True
                dq.append((ny, nx))

N = int(input())
boardRGB, boardRB = [], []
for _ in range(N):
    tmp1, tmp2 = [], []
    for i in input().rstrip():
        tmp1.append(i)
        i = 'R' if i == 'G' else i
        tmp2.append(i)
    boardRGB.append(tmp1)
    boardRB.append(tmp2)
visitedRGB = [[False] * N for _ in range(N)]
visitedRB = [[False] * N for _ in range(N)]

RGB, RB = 0, 0
for i in range(N):
    for j in range(N):
        if not visitedRGB[i][j]:
            visitedRGB[i][j] = True
            RGB += 1
            solution(i, j, visitedRGB, boardRGB)
        if not visitedRB[i][j]:
            visitedRB[i][j] = True
            RB += 1
            solution(i, j, visitedRB, boardRB)
print(RGB, RB)


# Fail Code
# from collections import deque
# import sys
# input = sys.stdin.readline

# def solution(y, x, std):
#     global board, visited
#     RGB_dict = {'R':'G', 'G':'R', 'B':'B'}
#     compare = RGB_dict[std]
#     dq = deque([(y, x, std)])
#     split = False
#     while dq:
#         y, x, std = dq.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny in range(N) and nx in range(N) and not visited[ny][nx]:
#                 if board[ny][nx] == std:
#                     visited[ny][nx] = True
#                     dq.append((ny, nx, std))
#                 elif board[ny][nx] == compare:
#                     split = True
#     return 1 if split else 0

# N = int(input())
# board = [input().rstrip() for _ in range(N)]
# visited = [[False]*N for _ in range(N)]
# dy = [-1, 0, 1, 0]
# dx = [0, -1, 0, 1]
# normal_cnt, split_cnt = 0, 0
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             visited[i][j] = True
#             split_cnt += solution(i, j, board[i][j])
#             normal_cnt += 1
# print(normal_cnt, normal_cnt-split_cnt)