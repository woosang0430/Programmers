def gcd(n, m):
  n, m = max(n, m), min(n, m)
  while m:
    temp = n%m
    n, m = m, temp
  return n

def solution(arr):
  ret = arr[0]

  for i in range(1, len(arr)):
    ret = ret * arr[i] // gcd(ret, arr[i])
  
  return ret

"""
입력값 : [2,6,8,14]
출력값 : 168
"""
