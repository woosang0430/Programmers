import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())

    floor = n%h
    num = n//h + 1
    if not floor:
        floor = h
        num = n//h

    print(str(floor) + str(num).zfill(2))