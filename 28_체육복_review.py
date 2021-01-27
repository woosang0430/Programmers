def solution(n, lost, reserve):
    # 체육복을 잃어 버렸지만 여분이 있는 친구가 있어 lost, reserve를 재정의한다.
    new_reserve = [i for i in reserve if i not in lost]
    new_lost = [i for i in lost if i not in reserve]

    for i in new_reserve: # 여분이 남는 친구의 앞뒤를 확인
        if i-1 in new_lost: # 앞에 친구가 없으면 빌려주기
            new_lost.remove(i-1)
        elif i+1 in new_lost: # 뒤에 친구가 없으면 빌려주기
            new_lost.remove(i+1)

    # new_lost에 남아있는 친구는 빌리지 못한 친구
    return n - len(new_lost)