import sys
sys.stdin = open('input.txt', 'rt')

from itertools import combinations

limit, _len = map(int, input().split())
num_list = list(range(1, limit+1))
for answer in combinations(num_list, _len):
    for i in answer:
        print(i, end=' ')
    print()