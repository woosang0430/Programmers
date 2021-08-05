import heapq
import sys
input = sys.stdin.readline

N = int(input())

num_list = [int(input()) for _ in range(N)]
heapq.heapify(num_list)

answer = 0
while len(num_list) > 1:
    a = heapq.heappop(num_list)
    b = heapq.heappop(num_list)
    tmp = (a + b)
    answer += tmp
    heapq.heappush(num_list, tmp)
print(answer)
