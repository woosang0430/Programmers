def solution(s):
  x = list(map(int, s.split()))
  ret = str(min(x)) + " " + str(max(x))
  return ret

"""
입력값 : -1 -2 -3 -4	
출력값 : -4 -1
"""