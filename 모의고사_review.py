answers = [1,2,3,4,5]
p = [[1,2,3,4,5],
[2,1,2,3,2,4,2,5],
[3,3,1,1,2,2,4,4,5,5]
]

chk = [0] * len(p)
# 학생별 맞춘 갯수 초기화

for num, answer in enumerate(answers):
    for i, v in enumerate(p):
        if answer == v[num % len(v)]:
    #         def dict_tests(lst, len_answer):
    #           if len_answer % len(lst) != 0:
    #               test_lst = lst * (len_answer//len(lst)) + lst[:len_answer%len(lst)]
    #           else:
    #                test_lst = lst * (len_answer//len(lst))

    #           return {k:v for k, v in enumerate(test_lst)}
            chk[i] += 1

print([i+1 for i, v in enumerate(chk) if v == max(chk)])
# dict_supoja = dict(zip(range(1,len(chk)+1), chk))
# sorted(dict_supoja.values())
# winner = [k for k, v in dict_supoja.items() if max(dict_supoja.values()) == v]
# print(winner)