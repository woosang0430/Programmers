""""
풀이 컨셉
- 각 열과 행의 index에 3의 거듭제곱을 나눈 몫에서 3을 나눈 나머지가 1인 경우가 공백으로 바꿔주는 방식으로 접근
- 전체가 별로 채워진 배열을 만들고 위의 규칙을 이용해 공백을 뚫어주는 방식
N = 3인 경우
(1, 1), (1, 4), (1, 7)
(4, 1), (4, 4), (4, 7)
,...   , ...   , ...

N = 9인 경우
(3, 3) ~ (3, 5)
(5, 3) ~ (5, 5)
,...  ~ ...

N = 27인 경우
(9, 9) ~ (9, 17)
(17, 9) ~ (17, 17)
,... ~ ...

식
(idx//num)%3 == 1
## 결과적으로 시간초과
"""

def space(i:int, j:int, num:int) -> None:
  if ((i//num)%3 == 1) and ((j//num)%3 == 1):
    array[i][j] = " "
  else:
    if array[i][j] == "*" and num // 3 != 0:
      space(i, j, num//3)

if __name__  == "__main__":
  import sys
  sys.stdin = open("input.txt", "rt")

  N = int(input())
  array = [["*"]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if array[i][j] == "*":
        space(i, j, N//3)

  for star in array:
    print(*star)

# ##########################
# def space(i:int, j:int, num:int) -> None:
#   if ((i//num)%3 == 1) and ((j//num)%3 == 1):
#     print(" ", end=" ")
#   else:
#     if num // 3 != 0:
#       space(i, j, num//3)
#     else:
#       print("*", end=" ")

# if __name__  == "__main__":
#   import sys
#   sys.stdin = open("input.txt", "rt")

#   N = int(input())

#   for i in range(N):
#     for j in range(N):
#       space(i, j, N//3)
#     print()
