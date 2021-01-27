"""
1. 주어진 수를 전부 True로 초기화
2. 1을 제외한 첫번째 소수 2부터 반복문
3. 주어진 수들 중 2의 배수를 False로 재정의한다.
    2*2, 2*3, 2*4 ..... 3*2, 3*3 ......
4. n개까지 반복(n의 제곱은 까지 구한다면 나머지 뒤쪽도 알 수 있다.)
5. 2~n개까지 반복문을 돌려 bool배열 중 True만 count or append
"""
def find_prime_num(n):
    arr = [True for i in range(n+1)] # 1번

    prime_nums = []

    for i in range(2,int(n**(1/2))+1): # 2번
        if arr[i]:
            j = 2
            while i*j <= n:
                arr[i*j] = False # 3번
                j +=1
    # cnt = 0
    for i in range(2, n+1): # 5번
        if arr[i]:
            #cnt +=1
            prime_nums.append(i)

    return prime_nums #or cnt
