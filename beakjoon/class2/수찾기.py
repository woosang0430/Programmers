import sys
input = sys.stdin.readline

N = input()
N_list = set(input().split())
M = input()
M_list = list(input().split())

for m in M_list:
    print(1) if m in N_list else print(0)