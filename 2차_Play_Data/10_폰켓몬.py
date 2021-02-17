def solution(nums):
    half = len(nums)//2
    set_nums = set(nums)
    if len(set_nums) >= half:
        answer = half
    else:
        answer = len(set_nums)
    return answer

# 다른 사람 풀이
def solution(nums):
    return min(len(nums)/2, len(set(nums)))