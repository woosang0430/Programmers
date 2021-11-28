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

# 재귀를 이용한 완전 탐색
# 파라미터로 현재의 값을 더한 경우와 더하지 않은 경우로 재귀를 돌린다.
# idx가 리스트의 index를 넘기는 것을 종료조건으로 한다
def solution(idx:int, sub_sum:int) -> None:
    global answer

    if idx == N: return

    sub_sum += number_list[idx]
    if sub_sum == goal:
        answer += 1

    solution(idx+1, sub_sum)
    solution(idx+1, sub_sum - number_list[idx])

if __name__  == "__main__":
    N, goal = map(int, input().split())
    number_list = list(map(int, input().split()))
    answer = 0
    solution(0, 0)

    print(answer)
"""
input
5 0
-7 -3 -2 5 8

output
1
"""