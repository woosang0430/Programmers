'''
# input.txt
6
1 3 5 6 7 10 
'''

import sys
sys.stdin = open('input.txt', 'rt')

def DFS(idx:int) -> None:
  global answer
  if idx == n:
    made = sum([num_list[i] for i in range(n) if visited[i]])
    if made == (total-made):
      answer = True
    return
  visited[idx] = True
  DFS(idx+1)
  visited[idx] = False
  DFS(idx+1)

if __name__ == '__main__':
  n = int(input())
  num_list = list(map(int, input().rstrip().split()))
  total = sum(num_list)
  visited = [False] * n
  answer = False
  DFS(0)
  print('YES' if answer else 'NO')

import sys

def DFS(idx, sum):
  if idx == n:
    if sum == (total - sum):
      print('YES')
      sys.exit()
  elif sum > total//2:
    return
  else:
    DFS(idx+1, sum+num_list[idx])
    DFS(idx+1, sum)

if __name__ == '__main__':
  n = int(input())
  num_list = list(map(int, input().rstrip().split()))
  total = sum(num_list)
  DFS(0, 0)
  print('NO')
