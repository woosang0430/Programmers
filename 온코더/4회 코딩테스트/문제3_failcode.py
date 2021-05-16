A0 = 1
X = 1
Y = 1
M = 2
n = 10000

from itertools import permutations
import sys
sys.setrecursionlimit(100000)

result = []
def func(n):
    if n == 0:
        result.append(A0)
        return A0
    temp = (func(n-1) * X + Y) % M
    result.append(temp)
    return temp

func(n-1)
result = set(result)
ret = float('inf')
if len(result) != 1:
    for i, j in permutations(result, 2):
        temp = abs(i-j)
        if temp < ret:
            ret = temp
else:
    ret = 0

print(ret)

# -----------------------------------------

A0 = 3
X = 7
Y = 1
M = 101
n = 5

from itertools import permutations

result = [A0]
ret = float('inf')

for i in range(1, n):
    temp = (result[-1] * X + Y) % M
    if temp == result[-1]:
        break
    elif temp == 0:
        ret = A0 - 1
        break
    result.append(temp)
if ret == float('inf'):
    if len(result) not in [1, 2]:
        for i, j in permutations(result, 2):
            temp = abs(i-j)
            if temp < ret:
                ret = temp
    else:
        ret = 0

print(ret)