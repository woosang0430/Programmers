def solution(s):
    strnum_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8',
                'nine':'9', 'zero':'0'}
    num = '0123456789'
    
    start, end = 0, 0
    ret = ''
    while end != len(s)+1:
        cur_num = s[start:end]
        if cur_num in strnum_dict.keys():
            ret += strnum_dict[cur_num]
            start = end
        elif cur_num in num:
            ret += cur_num
            start = end
        end += 1
    return int(ret)

s = "2three45sixseven"
print(solution(s))