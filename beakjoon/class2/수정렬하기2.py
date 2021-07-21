import sys

N = int(input())

num_list = sorted([int(sys.stdin.readline()) for _ in range(N)])
print('\n'.join(map(str, num_list)))