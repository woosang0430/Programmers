import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = int(input())
apple_list = [int(input()) for _ in range(l)]

# 시작값과 끝나는 값 초기화
start, end = 1, m
cnt = 0

# 범위 안에 들어오는 친구들은 무시
for i in apple_list:
    if start > i:
        # 시작점이 사과의 위치보다 크면 사과위치를 시작점으로 맞춤
        cnt += (start - i)
        start = i
        end = i + (m-1)
    elif i > end:
        # 끝점이 사과의 위치보다 크면 사과위치를 끝점으로 맞춤
        cnt += (i - end)
        start = i - (m-1)
        end = i

print(cnt)