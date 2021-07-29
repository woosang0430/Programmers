import sys
input = sys.stdin.readline

N = int(input())
floor_value = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(floor_value[1])
    sys.exit()

dp = [0] * (N+1)
dp[1] = floor_value[1]
dp[2] = floor_value[1]+floor_value[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-3] + floor_value[i-1] + floor_value[i], dp[i-2] + floor_value[i])

print(dp[-1])