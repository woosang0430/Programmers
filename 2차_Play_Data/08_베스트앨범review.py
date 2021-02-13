def solution(genres, plays):
    dic_plays = {i:v for i, v in enumerate(plays)}
    set_genres = set(genres)

    total_play = []
    for i in set_genres:
        temp, temp2 = [], []
        for k, v in dic_plays.items():
            if i == genres[k]:
                temp.append((k,v))
                temp2.append(v)
        temp.append(sum(temp2))
        total_play.append(temp)

    total_genres = sorted(total_play, key= lambda x: -x[-1])

    result = []
    for v in total_genres:
        v.pop() 
        v.sort(key=lambda x: (-x[1], x[0]))
        if len(v) == 1:
            result.append(v[0][0])
        else:
            for i in range(2):
                result.append(v[i][0])
    return result

print(solution(['classic', 'pop', 'classic', 'classic', 'pop', 'jpop'], [500, 600, 150, 800, 2500, 3000]))
# 결과값 : [4,1,5,3,0]
