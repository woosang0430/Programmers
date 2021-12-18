# [ATM](https://www.acmicpc.net/problem/11399)
- 은행 업무가 낮은 사람이 먼저 업무를 보는 것이 이득이므로 시간을 오름차순 순서로 나열한다.
- 자신의 차례가 될 때의 시간과 자신의 시간을 합해 하나의 리스트에 담은 후 전부 합해준다.

```python
import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
people = sorted(map(int, input().split()))

answer = []
temp = 0
for person in people:
    temp += person
    answer.append(temp)
print(sum(answer))
```