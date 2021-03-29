n, l = map(int, input().split())
location = sorted(list(map(int, input().split())))

compare = location[0]
cnt = 1
for i in range(1, n):
    if location[i] >= compare+l:
        compare = location[i]
        cnt += 1
        
print(cnt)