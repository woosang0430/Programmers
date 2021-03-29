n = int(input())
road_list = list(map(int, input().split()))
node_list = list(map(int, input().split()))

compare = float('inf')
min_price = min(node_list[:-1])
price = 0

for i in range(n):
    cur = node_list[i]
    if cur == min_price:
        price += cur * sum(road_list[i:])
        break
    compare = min(compare, cur)
    price += compare * road_list[i]
print(price)
## 함수 최소화하는 거 연습
## 더 생각하고 코드 짜자
###############################################33
n = int(input())
road_list = list(map(int, input().split()))
nodes = list(map(int, input().split()))

price = 0
cur = nodes[0]
for i in range(n-1):
    if nodes[i] <= cur:
        cur = nodes[i]
    price += cur * road_list[i]

print(price)