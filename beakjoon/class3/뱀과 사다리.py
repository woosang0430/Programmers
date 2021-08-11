import sys
from typing import List
sys.stdin = open('input.txt', 'rt')

from collections import deque

N = sum(map(int, input().split()))
ladder_info = dict()
for _ in range(N):
    a, b = map(int, input().split())
    ladder_info[a] = b
board = [-1] * 101
board[1] = 0

def solution(loc: int) -> int:
    global board, ladder_info
    dq = deque([loc])
    while dq:
        curr = dq.popleft()
        for i in range(1, 7):
            next = curr + i
            next = ladder_info[next] if next in ladder_info.keys() else next
            if next == 100:
                return board[curr] + 1
            elif 101 > next and board[next] == -1:
                board[next] = board[curr] + 1
                dq.append(next)
print(solution(1))


# from collections import deque

# def solution(loc: int, _cnt: int) -> int:
#     global visited, ladder_info
#     dq = deque([(loc, _cnt)])
#     while dq:
#         loc, cnt = dq.popleft()
#         if loc == 100:
#             return cnt
#         visited[loc] = True
#         for i in range(1, 7):
#             curr = loc + i
#             if curr in ladder_info.keys():
#                 curr = ladder_info[curr]
#             elif 101 > curr and not visited[curr]:
#                 dq.append((curr, cnt+1))

# N, M = map(int, input().split())
# ladder_info = dict()
# for _ in range(N+M):
#     s, e = map(int, input().split())
#     ladder_info[s] = e
# visited = [False] * 101
# print(solution(1, 0))