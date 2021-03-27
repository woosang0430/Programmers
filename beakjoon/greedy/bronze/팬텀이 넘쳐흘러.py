import sys
input = sys.stdin.readline

n = int(input())
start, end = [], []
for _ in range(n):
    i, j = map(int, input().split())
    start.append(i)
    end.append(j)

if max(end) >= min(start):
    print(0)
else:
    print(min(end) - max(start))

########################################################3

import sys
input = sys.stdin.readline

n = int(input())
time_range = [tuple(map(int, input().split())) for _ in range(n)]

time_range.sort()
result = 0
for i in range(1, n):
    if time_range[i-1][1] >= time_range[i][0]:
        continue
    result += time_range[i][0] - time_range[i-1][1]
print(result)