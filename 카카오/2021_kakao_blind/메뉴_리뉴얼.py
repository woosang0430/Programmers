from itertools import combinations
from typing import List

def possible_cnt(orders: List[int], case_menu: List[int]) -> int:
    cnt = 0 # 주문 횟수 (possible_limit update 예정)
    for order in orders:
        for menu in case_menu: 
            if menu not in order:
                break # 메뉴가 안들어있으면 break
        else: # 정상적으로 끝났으면 cnt += 1
            cnt += 1
    return cnt

def solution(orders, course):
    answer = []
    all_menu = list(set(''.join(orders))) # 중복제거된 모든 메뉴들
    for course_len in course:
        tmp = []
        possible_limit = 2 # 최소 2명 이상 부터!
        for case_menu in combinations(all_menu, course_len):
            cnt = possible_cnt(orders, case_menu)
            # 기존 보다 더 크면 limit와 menu 갱신
            if cnt > possible_limit:
                possible_limit = cnt
                tmp.clear()
                tmp.append(case_menu)
            # 같은 경우는 그냥 append
            elif cnt == possible_limit:
                tmp.append(case_menu)
        answer.extend(tmp)
    answer = list(map(''.join, sorted(map(sorted, answer))))
    return answer

a = ["XYZ", "XWY", "WXA"]
b = [2,3,4]
print(solution(a, b))

################################################################################

from itertools import combinations

def solution(orders, course):
    answer = []
    max_order = max(map(len, orders))
    for course_len in course:
        if course_len > max_order: # 최대 order을 넘으면 끝내기
            break
        total_case = dict()
        for order in orders: # 모든 경우에 대해 check
            for case in combinations(order, course_len):
                case = ''.join(sorted(case))
                if case not in total_case.keys():
                    # 처음이면 1로 초기화
                    total_case[case] = 1
                else:
                    # 있으면 + 1
                    total_case[case] += 1
        max_cnt = max(total_case.values()) # 해당 case의 최빈값
        for case, cnt in total_case.items():
            if cnt > 1 and cnt == max_cnt: # 2번 이상 주문했고 최빈값이면 추가
                answer.append(case)
    answer.sort()
    return answer

a = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
b = [2,3,4]
print(solution(a, b))

################################################################################

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for course_len in course:
        tmp = []
        for order in orders:
            tmp.extend(combinations(sorted(order), course_len))
        counter = Counter(tmp)
        if len(counter) != 0 and max(counter.values()) > 1:
            answer.extend([''.join(case) for case, value in counter.items() if max(counter.values()) == value])
    answer.sort()
    return answer

a = ["XYZ", "XWY", "WXA"]
b = [2,3,4]
print(solution(a, b))