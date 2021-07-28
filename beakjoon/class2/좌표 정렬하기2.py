import sys
input = sys.stdin.readline

n = int(input())
result_list = [list(map(int, input().split())) for _ in range(n)]
result_list.sort(key=lambda x: (x[1], x[0]))

for i, j in result_list:
    print(i, j)