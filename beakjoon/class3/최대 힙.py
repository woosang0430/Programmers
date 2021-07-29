import heapq
import sys
input = sys.stdin.readline

tmp = []
for _ in range(int(input())):
    n = int(input())
    if not n and not tmp:
        print(0)
    elif not n:
        print(-heapq.heappop(tmp))
    else:
        heapq.heappush(tmp, -n)