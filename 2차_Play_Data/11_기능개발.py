def solution(progresses, speeds):
    finish = []
    for i in range(len(speeds)):
        remnant = 100 - progresses[i]
        if remnant%speeds[i] == 0:
            finish.append(remnant//speeds[i])
        else:
            finish.append(remnant//speeds[i]+1)
            
    cnt, ret = 0, []
    x = finish[0]
    for i in range(1, len(finish)):
        cnt += 1
        if x < finish[i]:
            ret.append(cnt)
            cnt, x = 0, finish[i]
    ret.append(cnt+1)
    return ret