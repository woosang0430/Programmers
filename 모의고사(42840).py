## 학생 답안지 만들어 dictionary로 반환하는 함수
def dict_tests(lst, len_answer):
    if len_answer % len(lst) != 0:
        test_lst = lst * (len_answer//len(lst)) + lst[:len_answer%len(lst)]
    else:
        test_lst = lst * (len_answer//len(lst))

    return {idx:val for idx, val in enumerate(test_lst)}

p1 = [1,2,3,4,5]
p2 = [2,1,2,3,2,4,2,5]
p3 = [3,3,1,1,2,2,4,4,5,5]
answer = [1,2,3,4,5]

supoja = [p1, p2, p3]
lst_dict = [dict_tests(i, len(answer)) for i in supoja]
# 수포자들 답(list)들 dictionary로 묶기

dict_chart = {idx:val for idx, val in enumerate(answer)}
# 정답지 dictionary 
chk_lst = [0,0,0] # 수포자 1번 부터 맞춘 갯수 count check

for i in range(len(lst_dict)): # for문으로 한명씩 정답확인
    cnt = 0
    for j in range(len(dict_chart)):
        if  lst_dict[i][j] == dict_chart[j]:
            cnt+=1
    chk_lst[i] = cnt

dict_supoja = dict(zip(range(1,4), chk_lst))
sorted(dict_supoja.values())
# (학생 번호:맞춘 갯수 ) dict로 묶고 오름차순하기

winner = [k for k, v in dict_supoja.items() if max(dict_supoja.values()) == v]
# 제일 많이 맞춘 사람 추리기
print(winner)