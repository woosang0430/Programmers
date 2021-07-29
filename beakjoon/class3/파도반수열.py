import sys
input = sys.stdin.readline

dq = {0:0, 1:1, 2:1, 3:1, 4:2}
for i in range(5, 110):
    dq[i] = dq[i-5] + dq[i-1]

for _ in range(int(input())):
    n = int(input())
    print(dq[n])