from collections import deque
import sys
input = sys.stdin.readline

def cmdD(n): return 2*n%10000
def cmdS(n): return n-1 if n else 9999
def cmdL(n): return (n % 1000) * 10 + n // 1000
def cmdR(n): return (n%10) * 1000 + n//10
def solution(num, goal):
    global cmd_dict
    dq = deque([(num, '')])
    visited = {num}
    while dq:
        x, xCmd = dq.popleft()
        for cmd, func in cmd_dict.items():
            tmp = func(x)
            if tmp not in visited:
                if tmp == goal: return xCmd + cmd
                visited.add(tmp)
                dq.append((tmp, xCmd+cmd))

T = int(input())
cmd_dict = {'D':cmdD, 'S':cmdS, 'L':cmdL, 'R':cmdR}
for _ in range(T):
    num, goal = map(int, input().split())
    print(solution(num, goal))

# from collections import deque
# import sys
# input = sys.stdin.readline

# def cmdD(n): return 2*int(n)%10000
# def cmdS(n): return int(n)-1 if n!='0' else 9999
# def cmdL(n): return int(n[1:] + n[0])
# def cmdR(n): return int(n[-1] + n[:-1])
# def solution(X, goal):
#     global cmd_dic
#     dq = deque([(X, '')])
#     visited = set()
#     while dq:
#         x, xCmd = dq.popleft()
#         for cmd, func in cmd_dic.items():
#             tmp = str(func(x))
#             if tmp not in visited:
#                 if tmp == goal: return xCmd + cmd
#                 visited.add(tmp)
#                 dq.append((tmp, xCmd+cmd))

# T = int(input())
# cmd_dic = {'D':cmdD, 'S':cmdS, 'L':cmdL, 'R':cmdR}

# for _ in range(T):
#     X, goal = input().split()
#     print(solution(X, goal))