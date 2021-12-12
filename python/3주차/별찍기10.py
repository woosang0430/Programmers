def space(i:int, j:int, num:int) -> None:
  if ((i//num)%3 == 1) and ((j//num)%3 == 1):
    array[i][j] = " "
  else:
    if num // 3 != 0:
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
