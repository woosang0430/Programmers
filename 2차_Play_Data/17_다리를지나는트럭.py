# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#   bridge_on_truck = []
#   time = 0
#   dq = deque(truck_weights)
#   while dq:
#     truck = dq.popleft()
#     if sum(bridge_on_truck) + truck <= weight:
#       bridge_on_truck.append(truck)
#       continue
      
#     time += bridge_length + (len(bridge_on_truck) - 1)
#     bridge_on_truck.clear()
#     bridge_on_truck.append(truck)
  
#   if len(bridge_on_truck) != 0:
#     time += bridge_length + (len(bridge_on_truck) - 1)

from collections import deque

bridge_length = 5
weight = 5
truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
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
