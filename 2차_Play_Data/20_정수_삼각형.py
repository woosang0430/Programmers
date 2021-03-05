def solution(triangle):
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: # 처음 값은 비교 대상 없음
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1: # 끝 값은 비교할 대상 없음
                triangle[i][j] += triangle[i-1][j-1]
            else: # 중간의 값들은 값이 두개가 나오기 때문에 더큰 값으로 설정한다.
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))