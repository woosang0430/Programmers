import sys
input = sys.stdin.readline

n = int(input())
result_list = [0] * 10001
for _ in range(n):
    num = int(input())
    result_list[num] += 1

for i in range(len(result_list)):
    if result_list[i]:
        for _ in range(result_list[i]):
            print(i)