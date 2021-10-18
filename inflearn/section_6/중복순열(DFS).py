'''
# input.txt
3 2
'''
import sys
sys.stdin = open('input.txt', 'rt')

from typing import List


def DFS(basket:List[int], depth:int) -> None:
  global answers, count
  if depth == level:
    print(*basket)
    count += 1
    return
  for i in range(1, N+1):
    basket.append(i)
    DFS(basket, depth+1)
    basket.pop()


if __name__ == '__main__':
  N, level = map(int, input().rstrip().split())
  count = 0
  DFS([], 0)
  print(count)

#########################################################

def DFS(depth:int) -> None:
  global count
  if depth == level:
    print(*basket)
    count += 1
    return
  for i in range(1, N+1):
    basket[depth] = i
    DFS(depth+1)

if __name__ == '__main__':
  N, level = map(int, input().rstrip().split())
  count = 0
  basket = [0] * level
  DFS(0)
  print(count)