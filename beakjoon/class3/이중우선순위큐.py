import sys, heapq
input = sys.stdin.readline

def solution(tmp_list):
    global visited
    while tmp_list and not visited[tmp_list[0][1]]:
        heapq.heappop(tmp_list)

for T in range(int(input())):
    min_h, max_h = [], []
    visited = [False] * 1000001
    for i in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'I':
            visited[i] = True
            heapq.heappush(min_h, (int(cmd[1]), i))
            heapq.heappush(max_h, (-int(cmd[1]), i))
        else:
            tmp = max_h if cmd[1] == '1' else min_h
            solution(tmp)
            if tmp:
                visited[tmp[0][1]] = False
                heapq.heappop(tmp)
        solution(max_h)
        solution(min_h)
    
    if min_h and max_h:
        print(-heapq.heappop(max_h)[0], heapq.heappop(min_h)[0])
    else:
        print('EMPTY')
