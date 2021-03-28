import sys
input = sys.stdin.readline

n = int(input())
levels = [int(input()) for _ in range(n)]

cnt = 0
prev = levels.pop()
for i in range(1, n):
    # 같은 수일 때도 체크하기
    if prev <= levels[-i]:
        cnt += levels[-i] - (prev-1)
        levels[-i] = prev-1

    prev = levels[-i]
print(cnt)

# reverse()함수를 왜 생각 못했지?...
###################################################

import sys
input = sys.stdin.readline

n = int(input())
levels = [int(input()) for _ in range(n)]

cnt = 0
prev = levels.pop()

for i in range(1, n):
    # 점수는 양수여야 되기때문에 prev가 1일 떄 예외 처리
    if prev == 1:
        cnt += (levels[-i] - 1)
        levels[-i] = 1
    # 높은 점수 -1 의 수를 만들고 그 차를 cnt
    elif prev < levels[-i]:
        cnt += levels[-i] - (prev-1)
        levels[-i] = prev-1
    prev = levels[-i]
print(cnt)
'''
fail code 같을 때를 생각하지 않음...
양수라는 말에 1을 예외처리 했으나 쓸모없는 코드...
'''