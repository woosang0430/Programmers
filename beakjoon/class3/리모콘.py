goal = int(input())
M = int(input())
remove_list = list(input().split()) if M else []
curr_channel = 100

answer = abs(curr_channel - goal)

for channel in range(1000000):
    for i in range(len(str(channel))):
        # 사용할 수 없는 값이면 넘기기
        if str(channel)[i] in remove_list:
            break
        # 요소의 전체 값을 순회했는지 확인
        elif len(str(channel)) -1 == i: 
            answer = min(answer, abs(channel-goal)+len(str(channel)))

print(answer)