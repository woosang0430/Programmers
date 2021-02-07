def solution(n):
  if n == 1:
    return 1
  
  a, b = 0, 1
  for _ in range(n-1):
    c = a + b
    a, b = b, c
    return c