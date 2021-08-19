import sys
sys.stdin = open('input.txt', 'rt')

import sys

people_cnt, party_cnt = map(int, input().split())
try:
    know_people = list(map(int, input().split()))[1:]
except:
    print(party_cnt)
    sys.exit()
party_group = [list(map(int, input().split()))[1:] for _ in range(party_cnt)]

visited = set()
know_people = set(know_people)
lie_party = [True] * party_cnt
while know_people:
    know_person = know_people.pop()
    if know_person not in visited:
        visited.add(know_person)
        for group_idx in range(len(party_group)):
            for person in party_group[group_idx]:
                if person == know_person:
                    know_people.update(party_group[group_idx])
                    lie_party[group_idx] = False
                    break
print(sum(lie_party))

############################################
############################################
############################################
# fail code
import sys
input = sys.stdin.readline

people_cnt, party_cnt = map(int, input().split())
try:
    know_people = list(map(int, input().split()))[1:]
except:
    print(party_cnt)
    sys.exit()

people_connect = {i:set() for i in range(1, people_cnt+1)}
party_group = []
know_people = set(know_people)
for _ in range(party_cnt):
    group = list(map(int, input().split()))
    cnt, group = group[0], group[1:]
    party_group.append(group)
    for i in range(cnt):
        people_connect[group[i]].update(group[:i]+group[i+1:])

# 이 부분이 문제 진실을 새로 알게된 친구를 기준으로 탐색을 안함
tmp = set()
for know_person in know_people: 
    tmp.update(people_connect[know_person])
know_people.update(tmp)

answer = 0
for group in party_group:
    for person in group:
        if person in know_people:
            break
    else:
        answer += 1
print(answer)