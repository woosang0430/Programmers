import sys
input = sys.stdin.readline

def func(l, p, v):
    ret = l * (v // p)
    if l < v % p:
        ret += l
    else:
        ret += (v%p)
    return ret

cnt = 0
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    cnt += 1
    print('Case {0}: {1}'.format(cnt, func(l, p, v)))