"""
1번째 풀이 무게제한을 넘지않게 묶어서 한번에 시간 계산해주기! 
문제점
- 트럭이 먼저 빠져나갔을 때 다음 트럭이 바로 못들어오게 된다...
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
  bridge_on_truck = []
  time = 0
  dq = deque(truck_weights)
  while dq:
    truck = dq.popleft()
    if sum(bridge_on_truck) + truck <= weight:
      bridge_on_truck.append(truck)
      continue
      
    time += bridge_length + (len(bridge_on_truck) - 1)
    bridge_on_truck.clear()
    bridge_on_truck.append(truck)
  
  if len(bridge_on_truck) != 0:
    time += bridge_length + (len(bridge_on_truck) - 1)
  return time + 1
######################################################################
bridge_length = 5
weight = 5
truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
"""
2번째 풀이
다리를 정의하여 트럭 한개 한개씩 확인하기
문제점
한개씩 확인하며 sum 함수의 사용으로 시간초과가 나온다.
"""
from collections import deque

truck_weights = deque(truck_weights)
bridge = [0 for _ in range(bridge_length)]
bridge = deque(bridge)

# 다리길이만큼 0으로 초기화

time = 0
while truck_weights:
  time += 1
  if sum(bridge) + truck_weights[0] <= weight: # 무게제한을 안넘으면
    truck = truck_weights.popleft() # 트럭 1번 출발~
    bridge.append(truck)
  else:
    bridge.append(0) # 무게제한에 걸리면 0을 넣어줘 트럭 이동 시키기
  bridge.popleft()

print(time)
######################################################################
bridge_length = 5
weight = 5
truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
"""
다른 사람 풀이 참고
sum함수를 대신하여 현재 다리위에 있는 트럭의 무게를 변수로 받아 매순간 재정의
"""
from collections import deque

curr_weight = 0
truck_weights = deque(truck_weights)
bridge = deque([0] * bridge_length)
# 다리길이만큼 0으로 초기화

time = 0
while len(bridge) != 0:
  time += 1
  curr_weight -= bridge.popleft() # 다리를 빠져나온 트럭 무게 빼주기
  if truck_weights:
    if curr_weight + truck_weights[0] <= weight:
      curr_weight += truck_weights[0] # 다리에 위에 있는 트럭 무게 총합
      bridge.append(truck_weights.popleft())
    else:
      bridge.append(0)
print(time)
