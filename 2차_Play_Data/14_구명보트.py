from collections import deque

people = [40, 60, 70, 80, 80]
limit = 110
people.sort()
people = deque(people)
boat = 0

while True:
  # 가벼운 사람과 무거운 사람 짝꿍
  if people[0] + people[-1] > limit:
    # 보트에 뒷사람만 넣고 가기
    boat += 1
    people.pop()
  else:
    # 보트에 두사람 넣고 출발
    boat += 1
    people.popleft()
    people.pop()
  # if len(people) == 2:
  if len(people) <= 2:
    # 구조 대기자가 2명 이하면 반복구조 끝
    break

# 마지막 구조 대기자들이 제한을 넘기면 2번 아니면 1번 구조
if sum(people) > limit:
  boat += 2
else:
  boat += 1
print(boat)