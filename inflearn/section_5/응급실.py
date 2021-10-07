# input.txt
# 5 2
# 60 50 70 80 90

import sys
sys.stdin = open('input.txt', 'rt')

from collections import deque

patient_cnt, my_turn = map(int, input().split())

Q = list(map(int, input().split()))
Q = [(v, i) for i, v in enumerate(Q)]
Q = deque(Q)
cnt = 0

while True:
  danger_rate, patient_number = Q.popleft()
  if any(danger_rate < rate for rate, _ in Q):
    Q.append((danger_rate, patient_number))
  else:
    cnt += 1
    if patient_number == my_turn:
      break
print(cnt)

###

# patient_cnt, my_turn = map(int, input().rstrip().split())
# patients = list(map(int, input().rstrip().split()))
# patients = [(v, i) for i, v in enumerate(patients)]

# dq = deque(patients)
# cnt = 0

# while dq:
#   danger_rate, p_cnt = dq.popleft()
#   max_rate = max(dq)[0]
#   if max_rate > danger_rate:
#     dq.append((danger_rate, p_cnt))
#   else:
#     cnt += 1
#     if p_cnt == my_turn:
#       break
# print(cnt)

# any, all 연습하자