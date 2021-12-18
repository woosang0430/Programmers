import sys
sys.stdin = open('input.txt', 'rt')

"""
bfs를 이용한 완전 탐색

초기값인 1, 2, 3 으로 deque 자료구조를 생성
1, 2, 3의 모든 경우를 누적시켜 가며 dq에 쌓아준다.
dq에서 뽑은 값이 목표로 하는 값이면 answer에 +1
아니면 목표 값이 될 때까지 값을 누적하며 다시 dq에 쌓아준다.
(goal을 넘는 값은 무시한다.)
"""

from collections import deque

for _ in range(int(input())):
    goal = int(input())
    answer = 0
    dq = deque([1,2,3])
    while dq:
        curr = dq.popleft()
        if curr == goal:
            answer += 1
            continue
        else:
            for i in range(1, 4):
                next = curr + i
                if next <= goal:
                    dq.append(next)
    print(answer)

"""
input
5
6
7
8
9
10

out
24
44
81
149
274
"""