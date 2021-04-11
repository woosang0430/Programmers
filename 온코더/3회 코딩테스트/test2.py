def solution(x):
    stick, cnt = 64, 0
    while stick:
        # stick이 x보다 크면 반으로 자르기
        if stick > x:
            stick //= 2
        # x랑 같거나 작으면 x 에서 stick만큼 빼주고 cnt 반복
        else:
            x -= stick
            cnt += 1

    return cnt

print(solution(2))