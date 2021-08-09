import sys
input = sys.stdin.readline

def solution(y: int, x: int, value: int, check: int) -> None:
    global visited, board, answer, max_value
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    if check == 4:
        answer = max(value, answer)
        return
    if value + (4 - check) * max_value < answer:
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny in range(Y) and nx in range(X):
            if visited[ny][nx] == False:
                visited[ny][nx] = True
                if check == 2:
                    solution(y, x, value+board[ny][nx], check+1)
                solution(ny, nx, value+board[ny][nx], check+1)
                visited[ny][nx] = False
    return

Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
visited = [[False]*X for _ in range(Y)]
max_value = max(map(max, board))

answer = float('-inf')
for i in range(Y):
    for j in range(X):
        visited[i][j] = True
        solution(i, j, board[i][j], 1)
        visited[i][j] = False
print(answer)