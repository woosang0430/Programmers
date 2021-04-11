def solution(statements):
    # 길이가 1이고 0이면 -1 반환
    if len(statements) == 1 and statements[0] == 0:
        return -1
    
    # 중복하고 count해주기
    set_state = set(statements)
    result = []
    for i in set_state:
        cnt = statements.count(i)
        if i == cnt:
            result.append(i)
        
    if len(result):
        ret = max(result)
    else:
        ret = 0
    return ret

s = [0, 1, 1]

print(solution(s))