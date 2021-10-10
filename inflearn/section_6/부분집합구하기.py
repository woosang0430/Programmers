'''
# input.txt
3
'''

import sys
sys.stdin = open('input.txt', 'rt')

def DFS(i):
  if i > n:
    print(*[idx for idx in range(len(visited)) if visited[idx] == 1])
    return
  visited[i] = 1
  DFS(i+1)
  visited[i] = 0
  DFS(i+1)

if __name__ == '__main__':
  n = int(input())
  visited = [0] * (n+1)
  DFS(1)
  
'''
# output
1 2 3
1 2
1 3
1
2 3
2
3

'''
