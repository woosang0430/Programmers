def solution(y1:int, x1:int, n:int) -> None:
  global answer

  escape = False
  for y in range(y1, y1+n):
    if escape:
      break
    for x in range(x1, x1+n):
      if papers[y][x] != papers[y1][x1]:
        n //= 2
        answer += '('
        solution(y1, x1, n)
        solution(y1, x1+n, n)
        solution(y1+n, x1, n)
        solution(y1+n, x1+n, n)
        answer += ')'
        escape = True
        break
  if escape == False:
    answer += papers[y1][x1]

if __name__ == "__main__":
  import sys
  sys.stdin = open("input.txt", "rt")
  input = sys.stdin.readline

  N = int(input())
  papers = [list(input().rstrip()) for _ in range(N)]

  answer = ''
  solution(0, 0, N)
  print(answer)
