# input.txt
# 8 3

import sys
sys.stdin = open('input.txt', 'rt')

from collections import deque

n, k = map(int, input().rstrip().split())
dq = deque(range(1, n+1))

while dq:
  for _ in range(k-1):
    dq.append(dq.popleft())
  answer = dq.popleft()
print(answer)

####

# warrior_cnt, limit_cnt = map(int, input().rstrip().split())
# visited = [True] * warrior_cnt
# turn = 0
# cnt = limit_cnt - 1
# while sum(visited) != 1:
#   if visited[turn]:
#     if cnt == 0:
#       visited[turn] = False
#       cnt = limit_cnt - 1
#     else:
#       cnt -= 1
#   turn = (turn + 1) % warrior_cnt
# answer = [i+1 for i, v in enumerate(visited) if v]
# print(answer[0])

## que 자료구조가 빠르다..