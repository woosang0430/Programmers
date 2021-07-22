import sys

N = int(input())

location_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
location_info.sort(key=lambda x: (x[0], x[1]))
for x, y in location_info:
    print(x, y)