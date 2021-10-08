'''
# input.txt
5
big
good
sky
blue
mouse
sky
good
mouse
big
'''

import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
plan = {input():1 for _ in range(N)}
for _ in range(N-1):
  plan[input()] = 0

for key, val in plan.items():
  if val == 1:
    print(key)
    break
