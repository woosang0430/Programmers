from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = [input() for _ in range(N)]
result.extend([input() for _ in range(M)])
result = Counter(result)

cnt = 0
answer = []
for name, value in result.items():
    if value == 2:
        answer.append(name[:-1])
        cnt += 1

answer.sort()
print(cnt, *answer, sep='\n')