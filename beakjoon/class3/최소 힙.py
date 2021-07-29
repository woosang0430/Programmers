import heapq
import sys
input = sys.stdin.readline

num_list = []
for _ in range(int(input())):
    n = int(input())
    if not n and not num_list:
        print(0)
    elif not num_list:
        print(heapq.heappop(num_list))
    else:
        heapq.heappush(num_list, n)