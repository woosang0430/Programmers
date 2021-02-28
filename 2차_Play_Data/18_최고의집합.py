def solution(n, s):
  if n >= s:
    return [-1]
  answer = []
  
  while n:
    answer.append(s//n)
    s -= s//n
    n -= 1

  return answer