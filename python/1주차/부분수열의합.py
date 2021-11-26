import sys
sys.stdin = open('input.txt', 'rt')

# 문제의 제한시간과 N의 크기가 크지 않아 
# 파이썬의 combinations를 활용한 완전탐색이 가능하다고 판단하였습니다.
# 입력받은 배열에 대해 1 ~ N까지의 모든 조합을 구한 후 목표로 하는 값을 찾는다.

from itertools import combinations

N, goal = map(int, input().split())
number_list = list(map(int, input().split()))
answer = 0
for i in range(1, N+1):
    for cases in combinations(number_list, i):
        if sum(cases) == goal:
            answer += 1

print(answer)

"""
input
5 0
-7 -3 -2 5 8

output
1
"""