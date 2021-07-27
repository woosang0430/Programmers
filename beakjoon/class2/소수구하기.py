n, m = map(int, input().split())

possible_list = [True] * (m+1)

for i in range(2, m+1):
    if possible_list[i]:
        if i >= n:
            print(i)
        tmp = i * 2
        while tmp <= m:
            possible_list[tmp] = False
            tmp += i