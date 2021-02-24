from collections import deque

n = 3
computers = [
    [1,1,0],
    [1,1,1],
    [0,1,1]
]

# 모든 노드의 방문 여부를 0으로 초기화
visited = [0] * n
dq = deque()
cnt = 0
while 0 in visited:
    # q에 방문하지 않은 노드를 넣는다.
    dq.append(visited.index(0))
    while dq:
        node = dq.popleft()
        visited[node] = 1 # 방문한 노드는 체크
        for i in range(n):
            # 노드와 연결되어 있는 노드 확인
            if visited[i] == 0 and computers[node][i] == 1:
                # 있다면 dq에 넣고 다시 진행
                dq.append(i)
    cnt +=1 # dq가 끊기면 네트워크 끊김 count +1
print(cnt)
#  결과값 : 1