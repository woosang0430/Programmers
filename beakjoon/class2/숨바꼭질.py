from collections import deque

n, k = map(int, input().split())
def solution(n, k):
    if n == k:
        return 0

    dq = deque([(n, 0)])
    visited = set()
    while dq:
        x, cnt = dq.popleft()
        if x == k:
            return cnt
        elif x not in range(k) or x in visited:
            continue
        cnt += 1
        dq.extend([(x+1, cnt), (x-1, cnt), (x*2, cnt)])
        visited.add(x)

print(solution(n, k))

# ------------------------------------------------

from collections import deque

n, k = map(int, input().split())
def solution(n, k):
    if n == k:
        return 0

    dq = deque([(n, 0)])
    visited = set()

    while dq:
        x, cnt = dq.popleft()
        for i in [x+1, x-1, x*2]:
            if i == k:
                cnt += 1
                return cnt
                # dq.clear()
                # break
            elif i < 0 or i > 100000 or i in visited:
                continue
            visited.add(i)
            dq.append((i, cnt+1))
    # print(cnt)

print(solution(n, k))
