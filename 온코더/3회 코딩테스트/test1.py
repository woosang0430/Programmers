def solution(goods):
    # 높은 수 부터 확인하기 위해 정렬
    goods.sort()
    ret, prev = 0, 0
    while goods:
        cost = goods.pop()
        prev += cost
        # 50이 넘으면 바로 할인
        if prev >= 50:
            ret += (prev - 10)
            prev = 0
        # 안넘으면 누적 ㄱㄱ
    ret += prev
    return ret

print(solution([5,3,15]))