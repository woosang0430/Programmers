import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

for i in range(n):
    ropes[i] = ropes[i] * (i+1)
print(max(ropes))


#############################################
import sys
input = sys.stdin.readline

n = int(input())
rope_list = [int(input()) for _ in range(n)]
rope_list.sort()
result = 0
for i in set(rope_list):
    idx = rope_list.index(i)
    x = i * len(rope_list[idx:])
    result = max(x, result)

print(result)

## 시간 초과...
# 최고한의 함수를 사용하여 문제 풀자..