def solution(s, n):
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    uper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = len(lower_alpha)
    ret_lst = []

    for i in s:
        if i.islower(): # i가 소문자면 lower_alpha에서 찾아 n을 더하기
            ret_lst.append(lower_alpha[(lower_alpha.index(i) +  n) % l]) 
            # 더한 값이 리스트를 안넘기게하기 위해 리스트의 길이랑 나누기

        elif i.isupper(): # i가 대문자면 uper_alpha에서 찾아 n을 더하기
            ret_lst.append(uper_alpha[(uper_alpha.index(i) + n) % l])
            # 더한 값이 리스트를 안넘기게하기 위해 리스트의 길이랑 나누기

        elif i == " ": # 공백 문자.. 놓치지 않을꺼에요..
            ret_lst.append(i)
    
    return "".join(ret_lst)
