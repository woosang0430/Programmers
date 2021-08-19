import sys
sys.stdin = open('input.txt', 'rt')

import heapq, sys
input = sys.stdin.readline

node_len, road_len = map(int, input().split())
start = int(input())
node_info = [[] for _ in range(node_len+1)] # index 0 무시하기 (node개수의 +1)
for _ in range(road_len):
    s, e, w = map(int, input().split())
    node_info[s].append((e, w)) # 갈 수 있는 노드와 비용 저장

cost_list = [float('inf')] * (node_len+1)
cost_list[start] = 0 # 시작값 초기화

check = []
heapq.heappush(check, (0, start)) # cost, node
while check:
    curr_cost, curr_node = heapq.heappop(check) # check안의 최소값 반환
    for next_node, next_cost in node_info[curr_node]:
        if curr_cost + next_cost < cost_list[next_node]:
            cost_list[next_node] = curr_cost + next_cost # 작은 값으로 갱신
            heapq.heappush(check, (cost_list[next_node], next_node))
for x in cost_list[1:]:
    print(x if x != float('inf') else 'INF') # inf가 그대로면 INF, 아니면 원래값 반환