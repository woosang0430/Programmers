from collections import deque

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
N = len(board) # board의 가로, 세로 길이

def bfs(start):
    dq = deque([start])
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    visited = {(0, 0):100}
    # 딕셔너리의 키로 방문 여부 확인하기
    result_list = []
    while dq:
        y, x, direction, cost = dq.popleft()
        # 좌표와 방향, 가격
        for i in range(4):
            price = 100
            ny = y + dy[i]
            nx = x + dx[i]
            # 갈 수 있는 곳이라면
            if ny in range(N) and nx in range(N) and board[ny][nx] == 0:
                # 이동 비용은 100원 이지만 방향이 바뀌면 500 + 하기
                if i != direction:
                    price = 600
                cur_cost = cost + price
                # 방문하지 않았거나, 이전에 방문했을 때 보다 금액이 낮으면 dq에 넣기
                if (ny, nx) not in visited.keys() or visited[(ny, nx)] > cur_cost:
                    visited[(ny, nx)] = cur_cost
                    dq.append([ny, nx, i, cur_cost])
                    if ny == N-1 and nx == N-1:
                        # 종료조건은 리스트에 결과값만 넣어주기
                        result_list.append(cur_cost)
    return min(result_list)
    # 최소값을 반환해주기
start = [0, 0, 3, 0] # [y, x, direction, cost]

# 0, 0 에서 갈수 있는 방향은 아래와 오른쪽 밖에 없으므로 두개의 경우만 확인
answer1 = bfs([0, 0, 2, 0]) # [y, x, direcion, cost]
answer2 = bfs([0, 0, 3, 0])
print(min(answer1, answer2))

################################################################################################
from collections import deque

def solution(board):
    N = len(board)
    
    def bfs1(start):
        dq = deque([start])
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        visited = {(0, 0):100}
        result_list = []
        while dq:
            y, x, direction, cost = dq.popleft()
            for i in range(4):
                price = 100
                ny = y + dy[i]
                nx = x + dx[i]
                if ny in range(N) and nx in range(N) and board[ny][nx] == 0:
                    if i != direction:
                        price = 600
                    cur_cost = cost + price
                    if (ny, nx) not in visited.keys() or visited[(ny, nx)] > cur_cost:
                        visited[(ny, nx)] = cur_cost
                        dq.append([ny, nx, i, cur_cost])
                        if ny == N-1 and nx == N-1:
                            result_list.append(cur_cost)
        return min(result_list)
    
    down_start = bfs1([0, 0, 2, 0])
    right_start = bfs1([0, 0, 3, 0])
    
    return min(down_start, right_start)

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))