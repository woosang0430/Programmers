import sys
input = sys.stdin.readline

def solution(y1, x1, n):
    global papers, answer

    if not n:
        n = 1
    escape = False
    for y in range(y1, y1+n):
        if escape:
            break
        for x in range(x1, x1+n):
            if papers[y][x] != papers[y1][x1]:
                n //= 2
                answer += '('
                solution(y1, x1, n)
                solution(y1, x1+n, n)
                solution(y1+n, x1, n)
                solution(y1+n, x1+n, n)
                answer += ')'
                escape = True
                break
    if not escape:
        answer += papers[y1][x1]

N = int(input())
papers = [list(input()) for _ in range(N)]
answer = ''
solution(0, 0, N)
print(answer)

#############################################
# 시간 초과 코드

import sys
input = sys.stdin.readline

def solution(y, x, n):
    global board
    if not n:
        n = 1
    tmp = '('
    for y_start in [y, y+n]:
        for x_start in [x, x+n]:
            compare = board[y_start][x_start]
            for row in board[y_start:y_start+n]:
                if (len(set(map(int, row[x_start:x_start+n]))) != 1) or (compare != row[x_start]):
                    compare = solution(y_start, x_start, n//2)
            tmp += compare
    tmp += ')'
    return tmp

N = int(input())
board = [list((input())) for _ in range(N)]
print(solution(0, 0, N//2))