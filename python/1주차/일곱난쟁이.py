import sys
sys.stdin = open('input.txt', 'rt')

# 파이썬 내장함수인 combinations를 이용한 완전탐색
# but 효율성이 걱정..
from itertools import combinations
people = [int(input()) for _ in range(9)]

for seven in combinations(people, 7):
    if sum(seven) == 100:
        for answer in sorted(seven):
            print(answer)
        break

# 모범 풀이
# 오름차순으로 정렬한 후 일곱난쟁이가 아닌 친구들로 접근
# 미리 정렬 작업을 하여 나중에 정렬을 안해도된다.
from typing import List

def solution(people:List[int]) -> List[int]:
    for one in people:
        for two in people:
            if (one+two) == sum(people)-100:
                people.remove(one)
                people.remove(two)
                return people

people = sorted([int(input()) for _ in range(9)])
answer = solution(people)
for ans in answer:
    print(ans)

"""
input
20
7
23
19
10
15
25
8
13

output
7
8
10
13
19
20
23
"""
