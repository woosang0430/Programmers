from itertools import combinations
import sys

card_len, goal = map(int, input().split())
card_list = list(map(int, input().split()))

total_case = sorted(list(set(map(lambda x: sum(x), list(combinations(card_list, 3))))))
half = len(total_case)//2
start, end = 0, len(total_case)

while len(total_case[start:end]) != 1:
    if total_case[half] < goal:
        start = half
        half += (end - start) // 2
    elif total_case[half] > goal:
        end = half
        half -= (end - start) // 2
    else:
        print(total_case[half])
        sys.exit()
        break
print(total_case[start])

# from itertools import combinations
# import bisect

# card_len, goal = map(int, input().split())
# card_list = list(map(int, input().split()))
# total_case = sorted(list(map(lambda x: sum(x), combinations(card_list, 3))))

# idx = bisect.bisect_left(total_case, goal)
# if len(total_case) == 1 or total_case[idx] > goal:
#     idx -= 1
# print(total_case[idx])
## 런타임 에러.. 어디서 났을까?..