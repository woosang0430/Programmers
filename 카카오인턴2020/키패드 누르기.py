numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

dial_dict = dict()
for i in range(12):
    loc_info = (i//3, i%3)
    if i == 10: # 11은 0
        dial_dict[0] = loc_info
        continue
    dial_dict[i+1] = loc_info

def compare_num(dial_dict, num, left, right):
    cur_x, cur_y = dial_dict[num]
    left_x, left_y = dial_dict[left]
    right_x, right_y = dial_dict[right]
    compare_left = abs(cur_x-left_x) + abs(cur_y-left_y)
    compare_right = abs(cur_x-right_x) + abs(cur_x-right_y)
    return compare_left, compare_right

ret = []
left, right = 10, 12
for num in numbers:
    if num in [1, 4, 7]:
        left = num
        ret.append('L')
    elif num in [3, 6, 9]:
        right = num
        ret.append('R')
    else:
        compare_left, compare_right = compare_num(dial_dict, num, left, right)
        if compare_left < compare_right:
            left = num
            ret.append('L')
        elif compare_right < compare_left:
            right = num
            ret.append('R')
        else:
            if hand == 'left':
                left = num
                ret.append('L')
            else:
                right = num
                ret.append('R')
print(''.join(ret))

# [5, 8, 2, 5, 5]
#  R  R  R  R  R

#  L  L  R  R  L"