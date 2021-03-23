import sys
input = sys.stdin.readline # input은 시간차이 10배..

l = int(input())
time_range = [tuple(map(int, input().split())) for _ in range(l)]

# 끝나는 시간으로 1차 정렬 후 같으면 시작 시간으로 2차 정렬
time_range.sort(key=lambda x: (x[1], x[0]))

end_time, cnt = 0, 0 # 끝시간과 회의 횟수 초기화
for time in time_range:
    if end_time <= time[0]:
        # 끝 시간 업데이트
        end_time = time[1]
        cnt += 1
print(cnt)

'''
fail code 

문제점 (쓸데없는 이중 for문)
회의의 시작 시간이 아닌 종료시간을 기준으로 정렬을 못함
초반 회의 종료시간 초기화를 엉뚱한 것으로 초기화...
초기화는 0으로 하고 바로 업데이트해주자
'''
l = int(input())
time_range = [tuple(map(int, input().split())) for _ in range(l)]
# 회의 시작시간이 낮은 순으로 정렬
time_range.sort(key= lambda x: (x[0], x[1]))

result = 0
# 회의시간의 반만큼 비교
for i in range(len(time_range)//2):
    cnt = 1
    # 끝나는 시간에 회의 시작하는 팀있는지 확인
    compare_num = time_range[i][1]
    for j in time_range[i:]:
        if compare_num <= j[0]:
            # 비교할 시간 업데이트
            compare_num = j[1]
            cnt += 1
    # 오늘 회의한 팀 횟수 저장
    result = max(result, cnt)

# 제일 많이 쓸수 있는 스케줄
print(result)