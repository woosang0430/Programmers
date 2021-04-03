n = int(input())
s_list = [input() for _ in range(n)]

# 각 자릿수의 갯수 저장
compare = [0] * len(s_list[0])

# 이전 문자열과 같은 idx를 비교하면 같으면 compare의 같은 idx에 +
for i in range(1, len(s_list)):
    for j in range(len(s_list[i])):
        if s_list[i-1][j] == s_list[i][j]:
            compare[j] += 1

result = ''
for i in range(len(compare)):
    # 원래 리스트 보다 1개 적게 확인했으므로 n-1
    if compare[i] == n-1:
        result += s_list[0][i]
    # n-1이 아닌 인덱스에는 ?넣기
    else:
        result += '?'

print(result)