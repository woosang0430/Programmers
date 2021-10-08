'''
# input.txt
AKDEF
5
AYKGDHEJ
AQKWDERTFYP
CTFKSBDEA
ASKGHDEF
WOPASFKGHDEF
'''

import sys
sys.stdin = open('input.txt', 'rt')

from collections import deque

need = input()

for ts in range(1, int(input())+1):
  plans = input()
  dq = deque(need)
  for plan in plans:
    if plan in dq and plan != dq.popleft():
        print('#%d NO' % ts)
        break
  else:
    if len(dq) == 0:
      print('#%d YES' % ts)
    else:
      print('#%d NO' % ts)

# essential = input()

# for ts in range(1, int(input())+1):
#   plans = input()
#   compare = ''
#   check_idx = 0
#   for plan in plans:
#     if plan not in compare and plan in essential:
#       if plan == essential[check_idx]:
#         compare += plan
#         check_idx += 1
#       else:
#         print('#%d NO' % ts)
#         break
#   else:
#     if compare == essential:
#       print('#%d YES' % ts)
#     else:
#       print('#%d NO' % ts)