# 효율성이 안좋은 코드...
from itertools import permutations

n = 6
cnt = 0

# 3 이하면 자기자신
if n < 4:
    print(n)

# 0 ~ n 까지 타일을 가로로 할 수 있는 경우의 수만큼
for i in range(n//2 + 1):
    x = [1] * i
    y = [2] * (n - len(x)*2)
    temp = x + y # 갯수를 맞춘 리스트 들을 붙여준다.
    cnt += len(set(permutations(temp, len(temp)))) # 만들 수 있는 경우의 수를 더해준다.
"""
'2' : 0, '1' : 6  => 111111
'2' : 1, '1' : 4  => 21111
'2' : 2, '1' : 2  => 2211
'2' : 3, '1' : 0  => 222
"""
print(cnt)

### 결과값만 보면 피보나치 수열...
n = 6

a, b = 1, 2
for i in range(n-2):
    a, b = b, a+b
print(b)