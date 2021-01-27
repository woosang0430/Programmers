def solution(n, lost, reserve):
    # reserve와 lost에 곁치는 친구들을 구분해 새로운 배열(temp)에 담기
    # 체육복을 읽어버린 배열에서 여분 체육복이 있는 친구들 빼주기
    temp = [i for i in lost if i in reserve] 
    ret = n - (len(lost) - len(temp))

    # 체육복은 있으나 잃어 버린친구 재정의
    new_reserve = [i for i in reserve if i not in temp]
    new_lost = [i for i in lost if i not in temp]

    save_studn = []
    for i in new_lost:
        if i == 1:
            if i+1 in new_reserve:# 
                save_studn.append(new_reserve.pop(new_reserve.index(i+1)))
        elif i == n:
            if i-1 in new_reserve:
                save_studn.append(new_reserve.pop(new_reserve.index(i-1)))
        else:
            if i-1 in new_reserve:
                save_studn.append(new_reserve.pop(new_reserve.index(i-1)))
            elif i+1 in new_reserve:
                save_studn.append(new_reserve.pop(new_reserve.index(i+1)))

    return ret + len(save_studn)

print(solution(5,[2, 4],[3]))
