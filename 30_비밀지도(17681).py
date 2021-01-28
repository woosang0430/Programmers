def solution(n, arr1, arr2):
    def trans_launching(n, m): # 2진수로 바꿔주는 함수 정의
        ret = []
        while n:
            ret.append(n%2)
            n //= 2

        while len(ret) != m: # 2진수 길이 m이랑 맞추기 +0
            ret.append(0)

        ret = [i for i in ret[::-1]] # 역순으로 돌리기
        return ret
    
    # arr1, arr2 2진수로 바꾸기
    new_arr1 = [trans_launching(i, n) for i in arr1]
    new_arr2 = [trans_launching(i, n) for i in arr2]

    # 2진수의 arr1, arr2각 자리값 더해주기 result = [[20210]....]
    ret = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(new_arr1[i][j] + new_arr2[i][j])
        ret.append(temp)

    # ret에서 숫자가 0이면 " ", 아니면 "#"으로 리스트를 채운다.
    answer =[]
    for i in range(n):
        temp = []
        for j in ret[i]:
            if j != 0:
                temp.append("#")
            elif j == 0:
                temp.append(" ")
        answer.append("".join(temp)) # 각각의 값은 리스트를 벗긴다.
    return answer

"""
입력값 :
n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]

결과 : ['#####', '# # #', '### #', '#  ##', '#####']
"""