# 시간초과 3개, 실패 3개...
def solution(n,a,b):
    if a + 1 == b and b%2==0: # 예외처리
        return 1
    
    half = n // 2
    n += 1
    cnt = 0
    
    while n != 1:
        half +=1
        first = range(1, half)
        second = range(half, n)
        if (a in first and b in second) or (b in first and a in second):
            # 대진표를 반으로 나눈 양쪽에 a, b가 있다면 n이 1이 될때까지 나눠준다.
            while n != 1:
                cnt += 1
                n //= 2
        elif a in first and b in first:
        # 반으로 나눴는데 1 부터 half 몰려있으면 n과 half를 반으로 나눠가며 1번째 if문 안에 들어가도록한다.
            half, n = half//2, half
        elif a in second and b in second:
        # half 부터 끝까지 범위에 있는 a, b의 값은 half를 빼줘 2번째 elif문에 들어가도록한다.
            a -= half
            b -= half
            half, n = half//2, half
    return cnt

# 다른 사람 코드
def solution(n, a, b):
    cnt = 0
    #  a와 b가 출전하는 라운드를 2로 나눠어 갱신해준다.
    while a != b: # a와 b의 라운드 수가 같으면 
        cnt += 1
        a = (a+1) // 2
        b = (b+1) // 2
    return cnt

print(solution(8,4,7))


