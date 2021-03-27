s = input()

s = s.upper()
# 대문자로 비교하고 중복값 제거
s_set = set(s)
s_dict = dict()

# 단어는 key, 갯수는 value로 저장
for i in s_set:
    s_dict[i] = s.count(i)
values_list = list(s_dict.values())
# 많이 나온 알파벳 저장
max_num = max(values_list)

# 많이 나온 알파벳이 2개 이상이면 ?
if values_list.count(max_num) > 1:
    print('?')
# 아니라면 dict의 많은 값 반환
else:
    print(max(s_dict, key=lambda x: s_dict[x]))

"""
sort와 같이 max에서도 조회하고 싶은 기준을 정할 수 있다.
"""