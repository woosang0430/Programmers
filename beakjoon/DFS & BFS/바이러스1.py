# DFS
len_computer = int(input())
N = int(input())
computers = {i+1:set() for i in range(len_computer)}
for _ in range(N):
    x, y = map(int, input().split())
    computers[x].add(y)
    computers[y].add(x)

stack = [1]
visit = [False] * (len_computer+1)
visit[1] = True

while stack:
    virus = stack.pop()
    for i in computers[virus]:
        if visit[i] == False:
            visit[i] = True
            stack.append(i)
print(sum(visit)-1)

########################################################
# DFS
len_computer = int(input())
N = int(input())
node_list = [tuple(map(int, input().split())) for _ in range(N)]

visit = [False] * (len_computer + 1)
visit[1] = True
stack = [1]

while stack:
    virus = stack.pop()
    for i, j in node_list:
        if visit[i] and visit[j]:
            continue
        if virus == i:
            stack.append(j)
            visit[j] = True
        elif virus == j:
            stack.append(i)
            visit[i] = True
print(sum(visit)-1)

########################################################
# BFS
from collections import deque

len_computers = int(input())
N = int(input())
node_list = [tuple(map(int, input().split())) for _ in range(N)]

visit = [False] * (len_computers+1)
visit[1] = True
dq = deque([1])

while dq:
    virus = dq.popleft()
    for i, j in node_list:
        # 전염된 곳이면 건너뛰기
        if visit[i] and visit[j]:
            continue
        if virus == i:
            visit[j] = True
            dq.append(j)
        elif virus == j:
            visit[i] = True
            dq.append(i)
    
print(sum(visit)-1)