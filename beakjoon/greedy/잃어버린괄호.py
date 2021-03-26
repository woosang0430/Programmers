"""
fail code
어디가 문제이지 아직 잘 모르겠다..
테스트 케이스들을 돌리면 값은 제대로 나오지만
백준에서 돌리면 런타임...

컨셉 : 첫번째 마이너스를 기준으로 앞뒤로 두덩어리를 만든 후 두 덩어리 뻬기
"""
import re

s = input()
i = s.index('-')
x = sum(map(int, re.split('[+-]', s[:i])))
y = sum(map(int, re.split('[-+]', s[i+1:])))
print(x - y)
"""
위의 코드를 보강한 코드

컨셉은 찾지만 re모듈을 사용하지 않고 split으로 나누어가며 계산
"""
s = input().split('-')

x = sum(map(int, s[0].split('+')))
y = 0
for i in s[1:]:
    y += sum(map(int, i.split('+')))

print(x-y)