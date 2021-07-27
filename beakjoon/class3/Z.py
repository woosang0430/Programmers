n, y, x = map(int, input().split())

def find(y, x):
    prev_sq = 2**(n-1)
    curr_sq = 2**(n)
    if 0 <= y < prev_sq and 0 <= x < prev_sq:
        return 1
    elif 0 <= y < prev_sq and prev_sq <= x < curr_sq:
        return 2
    elif prev_sq <= y < curr_sq and 0 <= x < prev_sq:
        return 3
    else:
        return 4

def relocation(res):
    global n, y, x
    if res == 2:
        x -= 2**(n-1)
    elif res == 3:
        y -= 2**(n-1)
    elif res == 4:
        x -= 2**(n-1)
        y -= 2**(n-1)
    n -= 1

answer = 0
while n:
    res = find(y, x)
    answer += (res-1) * (4 ** (n-1))
    relocation(res)

print(answer)
