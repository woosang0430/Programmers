def solution(y1:int, x1:int, n:int) -> None:
  global answer
  y_split = [y1, y1+n, y1+(n*2)]
  x_split = [x1, x1+n, x1+(n*2)]
  for y_start in y_split:
    for x_start in x_split:
      possible = True
      compare = papers[y_start][x_start]
      for row in papers[y_start:y_start+n]:
        if len(set(row[x_start:x_start+n])) != 1 or compare != row[x_start]:
          solution(y_start, x_start, n//3)
          possible = False
          break
      if possible == True:
        idx = check.index(row[x_start])
        answer[idx] += 1


if __name__ == "__main__":
  import sys
  sys.stdin = open("input.txt", "rt")
  input = sys.stdin.readline

  N = int(input().rstrip())
  papers = [list(map(int, input().rstrip().split())) for _ in range(N)]
  check = [-1, 0, 1]
  answer = [0] * 3 # [-1, 0, 1] 정답의 각 case
  possible = True
  compare = papers[0][0]
  for row in papers:
    if len(set(row)) != 1 or compare != row[0]:
      solution(0, 0, N//3)
      possible = False
      break
  if possible:
    idx = check.index(row[0])
    answer[idx] += 1

  print(*answer, sep='\n')
