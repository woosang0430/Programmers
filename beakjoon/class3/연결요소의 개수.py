import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solution(node: int) -> None:
    global visited
    visited[node] = True
    for connect_node in node_info[node]:
        if visited[connect_node] == False:
            solution(connect_node)

N, M = map(int, input().split())
node_info = {i:set() for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    node_info[a].add(b)
    node_info[b].add(a)
visited = [False] * (N+1)

cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        solution(i)
        cnt += 1
print(cnt)

