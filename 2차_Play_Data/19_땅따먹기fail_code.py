# def solution(land):
#     answer, idx = 0, []
#     answer += max(land[0])
#     idx.append(land[0].index(max(land[0])))

#     for i in range(1, len(land)):
#         max_value = max(land[i])
#         max_idx = land[i].index(max_value)
        
#         if idx[-1] != max_idx:
#             answer += max_value
#             idx.append(max_idx)
#         else:
#             land[i][max_idx] = 0
#             answer += max(land[i])
#             idx.append(land[i].index(max(land[i])))

#     return answer

# x = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

# print(solution(x))


def solution(land):
    answer, idx = 0, 0
    answer += max(land[0])
    idx = land[0].index(max(land[0]))
    i = 1
    
    while i != len(land):
        # 중복되는 인덱스를 제외한 행의 제일 큰값만 저장
        max_value = max(land[i])
        max_idx = land[i].index(max_value)
        
        if idx == max_idx:
            land[i][max_idx] = 0
            continue
        answer += max_value
        idx = max_idx
        i += 1
        
    return answer

x = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

print(solution(x))
