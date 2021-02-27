skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

answer = 0

for i in skill_trees:
    check = ""
    for j in i:
        # 빼낸 스킬 한개씩 skill에 있는지 확인
        if j in skill:
            # 선행 스킬 찍음? 선행 스킬 확인 or skill 최하단 인지 확인
            if skill[skill.index(j) - 1] in check or j == skill[0]:
                check += j
            else:
                # 안찍었으면 break
                break
        # skill안에 없으면 선행스킬 없음
        else:
            check += j
    # 스킬 순서와 스킬이 맞으면 +1
    if check == i:
        answer += 1
print(answer)
