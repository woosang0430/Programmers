# 이전 코드 수정
from collections import deque

people = [40, 40, 50, 50, 60, 70, 80, 80]
limit = 110
people.sort()
people = deque(people)
boat = 0

while people:
  # 가벼운 사람과 무거운 사람 짝꿍
  if len(people) == 1:
    # 구조 대기자가 1명이면 반복구조 끝
    boat += 1
    break
  if people[0] + people[-1] > limit:
    # 보트에 뒷사람만 넣고 가기
    boat += 1
    people.pop()
  else:
    # 보트에 두사람 넣고 출발
    boat += 1
    people.popleft()
    people.pop()

print(boat)
######################################################
people = [40, 60, 70, 80, 80]
limit = 110

answer = 0
people.sort()

a = 0
b = len(people) - 1
while a < b:
  # 두명씩 탈 수 있는 경우의 수만 체크
  if people[b] + people[a] <= limit:
    answer += 1
    a += 1
  # 조건문을 탈 때 까지 뒷사람 변경
  b -= 1
# 리밋에 걸린 사람들은 혼자 타야되므로 원래 인원수에서 두명이 탔던 횟수 빼기
print(len(people) - answer)

# 1번 코드와 2번 코드의 성능 차이
"""
테스트 1 〉	통과 (11.22ms, 10.8MB)
테스트 2 〉	통과 (13.14ms, 10.8MB)
테스트 3 〉	통과 (11.27ms, 10.7MB)
테스트 4 〉	통과 (13.76ms, 10.8MB)
테스트 5 〉	통과 (12.28ms, 10.8MB)

테스트 1 〉	통과 (8.54ms, 10.7MB)
테스트 2 〉	통과 (9.53ms, 10.6MB)
테스트 3 〉	통과 (8.17ms, 10.5MB)
테스트 4 〉	통과 (9.28ms, 10.6MB)
테스트 5 〉	통과 (7.79ms, 10.6MB)
"""