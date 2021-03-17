# 각 요소 들을 따로따로 비교하면서 두개 중 한개가 들어가 있으면 연결된 것이다.
# 둘다 없으면 연결이 안된것
# 리스트에 연결된 것을 담아 주기

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# costs = [[1,2,13],[1,3,5],[2,4,9],[3,4,15],[3,5,3],[4,5,1],[4,6,7],[5,6,2]]

costs.sort(key=lambda x: x[-1]) # 비용 기준으로 오름차순 정렬
nodes = [costs[0][0], costs[0][1]] # 제일 싼 비용의 다리 넣고 비용 저장
node_cost = costs[0][2]

for i in range(1, len(costs)):
    if costs[i][0] in nodes and costs[i][1] in nodes:
        # 이미 지어진 다리면 pass
        continue
    # 한개의 도로만 연결되어 있으면 연결되지 않는 쪽 다리 만들기
    if costs[i][0] in nodes:
        nodes.append(costs[i][1])
    else:
        nodes.append(costs[i][0])
    # 비용 저장
    node_cost += costs[i][2]

print(node_cost)
########################################################3
parent = dict()
rank = dict()

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(costs, n):
    mst = list()

    # 1. 초기화
    for node in range(n):
        make_set(node)
    
    # 2. 비용을 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[-1])

    # 3. 간선 연결(사이클 없는)
    for cost in costs:
        node_v, node_u, price = cost
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(price)
    return sum(mst)

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(kruskal(costs, n))
###########################################################3
# 구글링 참고 코드
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def mykruskal(n, costs):
    mst = list()
    parent = dict()
    rank = dict()

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

    for i in range(n):
        parent[i] = i
        rank[i] = 0
    
    costs.sort(key=lambda x: x[-1])

    for info in costs:
        node1, node2, cost = info
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(cost)
    return sum(mst)

print(mykruskal(n, costs))
