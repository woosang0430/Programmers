n, k = 10, 5
k_location = [[1,5],[1,3],[1,2],[1,6],[1,7]] # 사과 위치
l = 4
second, location = [8, 10, 11, 13], ['D', 'D', 'D', 'L']
# for _ in range(l):
#   x, c = input().split()
#   second.append(x)
#   location.append(c)
# second_location = {int(i):v for i, v in zip(second, location)} # 시간과 방향
second_location = {8: 'D', 10: 'D', 11: 'D', 13:'L'}

map_arr = [[0]*n for _ in range(n)] # 맵

for i in range(k):
  map_arr[k_location[i][0]][k_location[i][1]] = 2 # 사과위치 정의
map_arr[0][0] = 1 # 뱀위치 정의
snake = [[0,0]] # 뱀 이동경로

dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = 1

def turn_left():
  global direction
  direction -= 1
  direction %= 4

def turn_right():
  global direction
  direction += 1
  direction %= 4
time = 0
x, y = 0, 0 

while True:
  time+=1

  nx = x + dx[direction]
  ny = y + dy[direction]
  if nx == -1 or nx == n or ny == -1 or ny == n:
    break

  if map_arr[nx][ny] == 2:
    map_arr[nx][ny] = 1
    # x, y = nx, ny
    snake.append([x,y])
  elif map_arr[nx][ny] == 0:
    map_arr[nx][ny] = 1
    snake.append([nx,ny])
    a, b = snake.pop(0)
    map_arr[a][b] = 0
    # x, y = nx, ny
  elif map_arr[nx][ny] == 1:
    break
  x, y = nx, ny
  if  time in second:
    if second_location[time] == "L":
      turn_left()
    else:
      turn_right()

print(time)