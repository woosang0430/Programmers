from itertools import permutations
import copy

def solution(expression):
    split_exp = []
    temp = ''
    # 연산자 기준으로 나눈 새로운 배열 생성
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            split_exp.append(temp)
            split_exp.append(i)
            temp = ''
    split_exp.append(temp)
    split_exp.append('0') # 슬라이싱 할때 에러 안나게 하기 위함
    
    # 필요없는 연산자 제거 과정
    operator = ''
    for i in ['-', '+', '*']:
        if i in expression:
            operator += i
            
    # 비교할 변수 생성, 모든 연산자의 경우를 확인
    ret = float('-inf')
    for case in permutations(operator, len(operator)):
        exp_copy = copy.deepcopy(split_exp)
        for oper in case:
            idx = 0
            while idx != len(exp_copy):
                if exp_copy[idx] == oper:
                    exp_copy[idx-1] = str(eval(''.join(exp_copy[idx-1:idx+2])))
                    exp_copy.pop(idx)
                    exp_copy.pop(idx)
                    continue
                idx += 1
        ret = max(ret, abs(int(exp_copy[0])))
        
    return ret