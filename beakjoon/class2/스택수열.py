import sys

N = int(input())
stack_list = []
answer_list = []
curr_num = 1
for _ in range(N):
    compare_num = int(input())
    while compare_num >= curr_num:
        stack_list.append(curr_num)
        answer_list.append('+')
        curr_num += 1
    if stack_list[-1] == compare_num:
        stack_list.pop()
        answer_list.append('-')
    else:
        print('NO')
        sys.exit()

for answer in answer_list:
    print(answer)
