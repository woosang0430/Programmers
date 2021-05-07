# final
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

unique_gems = len(set(gems))
len_gems = len(gems)
start, end = 0, 0 # 투포인트 지정
my_basket = {gems[0]:1} # 현재 얼만큼 가지고 있나
result = [0, len_gems]
while start < len_gems and end < len_gems:
    if len(my_basket) == unique_gems: # 모든 보석이 모이면
        if end - start < result[1] - result[0]:
            result = [start+1, end+1] # 더 짧은 길이 저장
        my_basket[gems[start]] -= 1
        if my_basket[gems[start]] == 0:
            del my_basket[gems[start]]
        start += 1
    else:
        end += 1
        if end == len_gems:
            break
        if gems[end] not in my_basket.keys():
            my_basket[gems[end]] = 1
        else:
            my_basket[gems[end]] += 1
        
print(result)

# 1
gems = ["AA", "AB", "AC", "AA", "AC"]

set_gems = set(gems)
end_idx, start_idx = 0, 0
new_gems = []
for i in range(len(gems)+1):
    if set(gems[:i]) == set_gems:
        end_idx = i
        break

for i in range(len(gems)):
    if set(gems[i:end_idx]) != set_gems:
        start_idx = i
        break
print([start_idx, end_idx])

# 2
gems = ["XYZ", "XYZ", "XYZ"]

set_gems = set(gems)
len_set_gems = len(set_gems)

start, end = 0, len_set_gems

while True:
    if end > len(gems):
        len_set_gems += 1
        start, end = 0, len_set_gems
    if set(gems[start:end]) == set_gems:
        break
    start += 1
    end += 1

print([start+1, end])

# 3
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

set_gems = set(gems) # 고유값
len_set_gems = len(set_gems) # 고유값의 길이
cnt_gems = [(gems.count(i), i) for i in set_gems]
min_gems = min(cnt_gems)[1] # 희소한 보석

def get_end_start(len_set_gems, idx=0):
    global gems, min_gems
    min_idx = gems.index(min_gems, idx)
    end = min_idx
    start = end - len_set_gems
    return end, start, min_idx

end, start, min_idx = get_end_start(len_set_gems)
while True:
    if start < 0:
        end += -start
        start = 0
    elif start > min_idx or end > len(gems):
        try:
            end, start, min_idx = get_end_start(len_set_gems, idx=min_idx+1)
            continue
        except:
            num = len_set_gems - len(set(gems[start:end]))
            len_set_gems += num
            end, start, min_idx = get_end_start(len_set_gems)
            continue
    if set(gems[start:end]) == set_gems:
        break
    start += 1
    end += 1
print([start+1, end])