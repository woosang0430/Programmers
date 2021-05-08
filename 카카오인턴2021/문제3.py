# Fail code

import copy
def solution(n, k, cmd):
    excel = [i for i in range(n)]
    remove_list = []
    excel_copy = copy.deepcopy(excel)
    for comand in cmd:
        if comand[0] == 'D':
            k += int(comand[-1])
        elif comand[0] == 'U':
            k -= int(comand[-1])
        elif comand[0] == 'C':
            if k == len(excel_copy)-1:
                k -= 1
                remove_list.append(excel_copy.pop())
            else:
                remove_list.append(excel_copy.pop(k))
        else:
            if remove_list:
                arrive = remove_list.pop()
                num_arrive = int(arrive)
                excel_copy.insert(num_arrive, arrive)
                if num_arrive < k:
                    k += 1
    
    answer = ''
    for i in excel:
        if i in excel_copy:
            answer += 'O'
        else:
            answer += 'X'
    
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))
# n	k	cmd	result
# 8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	"OOOOXOOO"
# 8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	"OOXOXOOO"