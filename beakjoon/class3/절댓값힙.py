import heapq

N = int(input())
tmp = []
for _ in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(tmp, (abs(n), n))
    else:
        if not tmp:
            print(0)
        else:
            print(heapq.heappop(tmp)[1])