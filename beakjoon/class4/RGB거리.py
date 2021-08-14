
import sys
sys.stdin = open('input.txt', 'rt')

import sys
input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])
print(min(rgb[-1]))




