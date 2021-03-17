n = 5
costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]

# 최소비용건설을 위해 비용 기준 정렬(그리디)
costs.sort(key=lambda x: x[-1])

# 건설 정보 초기화
nodes = {costs[0][0], costs[0][1]} # 중복값 제거 목적
price = costs[0][2]

# 모든 섬이 연결될때 까지
while len(nodes) != n:
  for i in range(1, len(costs)):
    node1, node2, cost = costs[i]
    # 둘중에 한개라도 연결되어있으면
    if node1 in nodes or node2 in nodes:
      # 둘다 연결되어있으면 무시
      if node1 in nodes and node2 in nodes:
        continue
      # 아니면 섬 연결
      else:
        nodes.update([node1, node2])
        price += cost
        # 처음 부터 확인
        break
        
print(price)
