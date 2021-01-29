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
            chk[i] += 1

print([i+1 for i, v in enumerate(chk) if v == max(chk)])
