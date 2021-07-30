from collections import deque
import sys
input = sys.stdin.readline
# readline으로 문자열받아 처리할때 위에 '\n' 제거하는거 잊지말기

for _ in range(int(input())):
    commands = input()[:-1]
    n = int(input())
    tmp = input()[1:-2]
    n_list = deque(tmp.split(',') if tmp else [])

    r_check = 0
    escape = True
    for command in commands:
        if command == 'R':
            r_check += 1
        else:
            if not n_list:
                escape = False
                break
            n_list.pop() if r_check%2 else n_list.popleft()
    if escape:
        n_list = list(n_list)
        n_list = n_list[::-1] if r_check%2 else n_list
        print('[%s]' % ','.join(n_list))
    else:
        print('error')