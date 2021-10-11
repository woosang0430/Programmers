'''
# input.txt
259 5
81
58
42
33
61
'''

import sys
sys.stdin = open('input.txt', 'rt')

def DFS(idx, sum, mid_sum):
  global answer
  if sum > limit or answer > sum + (total - mid_sum):
    return
  elif idx == dog_count:
    if sum > answer:
      answer = sum
  else:
    DFS(idx+1, sum+dogs[idx], mid_sum+dogs[idx])
    DFS(idx+1, sum, mid_sum+dogs[idx])

if __name__ == '__main__':
  limit, dog_count = map(int, input().rstrip().split())
  dogs = [int(input()) for _ in range(dog_count)]
  total = sum(dogs)
  answer = float('-inf')
  DFS(0, 0, 0)
  print(answer)