import heapq
import sys
input = sys.stdin.readline

num_list = []
for _ in range(int(input())):
    n = int(input())
    if not n:
        if num_list:
            print(heapq.heappop(num_list))
        else:
            print(0)
    else:
        heapq.heappush(num_list, n)