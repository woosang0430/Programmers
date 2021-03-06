"""
[접근법] DP

문제에서 이동결로는 아래, 오른쪽 밖에 없므로
현재 위치는 지나왔던 위쪽, 왼쪽의 값을 더해준다.
안지났거나 웅덩이같은 경우는 0 이므로 괜찮
y = row
x = column
결과값 = [y-1][x] + [y][x-1]
            ^         ^
         위의 값     왼쪽 값

- 처음 시작값을 1로 지정하여 시작
- 매 순간 위의 식으로 영역표시를 남겨주며 이동
- 웅덩이가 있을 경우 계산을 배제하기 위해 0으로 지정
"""
m, n = 4, 3
puddles = [[2,2]]

# 맵초기화
map_arr = [[0] * (m+1) for _ in range(n+1)]
# 처음 위치 영역표시
map_arr[1][1] = 1

for y in range(1, n+1):
    for x in range(1, m+1):
        # 처음 위치 표시 완료
        if y == 1 and x == 1:
            continue
        # 웅덩이는 표시를 못하므로 0으로 
        if [x, y] in puddles:
            map_arr[y][x] = 0
        # 웅덩이가 아니면 영역 표시 ㄱㄱ
        else:
            map_arr[y][x] = map_arr[y-1][x] + map_arr[y][x-1]
# 목적지는 위와 왼쪽값을 더해준다.
result = (map_arr[n-1][m] + map_arr[n][m-1]) % 1000000007
print(result)

# 다른 분 풀이1
m, n = 4, 3
puddles = [[2,2]]

answer = 0
route_map = [[0]*m for i in range(n)]
memo = [[0]*m for i in range(n)]
for p in puddles:
    route_map[p[1]-1][p[0]-1] = 1
memo[0][0] = 1
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if route_map[i][j] == 1:
            memo[i][j] = 0
        elif i == 0:
            memo[i][j] = memo[i][j-1]
        elif j == 0:
            memo[i][j] = memo[i-1][j]
        else:
            memo[i][j] = memo[i-1][j] + memo[i][j-1]
print(memo)
answer = memo[n-1][m-1]
print(answer)

# 다른 분 풀이 2
def solution(m, n, puddles):
    answer = 0
    info = dict([((2, 1), 1), ((1, 2), 1)]) # 초기 시작 값
    for puddle in puddles: # 웅덩이 좌표 가져오기
        info[tuple(puddle)] = 0 
        # key가 웅덩이 좌표인 value를 0으로 설정

    def func(m, n): # 최단 경로 재귀 함수
        if m < 1 or n < 1:
            return 0
        if (m, n) in info: # info에 key값이 (m, n)가 있으면
            return info[(m, n)] # 키 값에 대비되는 값을 반환
        # setdefault 사용
        # (m, n)이 존재하면 (m, n)을 반환, 아니면 2번째 인스턴스 반환
        # 2번째 인스턴스 == 재귀 함수
        return info.setdefault((m, n), func(m-1, n) + func(m, n-1))
    return func(m, n) % 1000000007