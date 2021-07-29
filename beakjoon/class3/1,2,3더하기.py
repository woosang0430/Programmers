from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dq = deque([1, 2, 3])
    answer = 0
    while dq:
        x = dq.pop()
        answer = answer + 1 if x == N else answer
        for i in range(1,4):
            tmp = x + i
            if tmp <= N:
                dq.append(tmp)
    print(answer)