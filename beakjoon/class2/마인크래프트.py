import sys
input = sys.stdin.readline

y, x, b = map(int, input().split())

start = float('inf')
end = float('-inf')
mine_map = []
for _ in range(y):
    arr = list(map(int, input().split()))
    mine_map.append(arr)
    start = min(min(arr), start)
    end = max(max(arr), end)

time = float('inf')
for compare in range(start, end+1):
    block = b
    remove_cnt, add_cnt = 0, 0
    for row in mine_map:
        for element in row:
            if compare < element:
                remove_cnt += abs(compare - element)
            elif compare > element:
                add_cnt += compare - element
    block += remove_cnt
    if block >= add_cnt:
        tmp = add_cnt + (remove_cnt * 2)
        if time >= tmp:
            time = tmp
            height = compare
print(time, height)

#######################################################################

from collections import Counter
import sys
input = sys.stdin.readline

y, x, b = map(int, input().split())

mine_map = []
for _ in range(y):
    mine_map.extend(list(map(int, input().split()))) 

count_map = Counter(mine_map)
time = float('inf')
answer = []

for height in range(min(count_map.keys()), max(count_map.keys())+1):
    inventory = b
    remove_cnt, add_cnt = 0, 0
    for value, cnt in count_map.items():
        if height < value:
            remove_cnt += abs(height - value) * cnt
        elif height > value:
            add_cnt += (height - value) * cnt
    inventory += remove_cnt
    if inventory >= add_cnt:
        time = add_cnt + (remove_cnt * 2)
        answer.append([time, height])

answer.sort(key=lambda x: (x[0], -x[1]))
print(answer[0][0], answer[0][1])