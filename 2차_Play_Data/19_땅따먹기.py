land = [[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]]

for row in range(1, len(land)):
    for i in range(4):
        rest = set(range(4)) - {i}
        land[row][i] += max([land[row-1][idx] for idx in range(4) if idx in rest])
print(max(land[-1]))

lst = []
for i in range(1, len(land)):
    for j in range(4):
        for k in range(4):
            # 인덱스가 중복되지 않도록 조건문으로 처리한다.
            if j != k:
                lst.append(land[i][j] + land[i-1][k])
        land[i][j] = max(lst)
        lst = []
print(max(land[-1]))

for i in range(1, len(land)):
    for j in range(4):
        # 중복되는 인덱스를 뺀 리스트를 만들고 그중 제일 높은 수를 더해준다.
        land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
print(max(land[-1]))

# for i in range(1, len(land)):
#     for j in range(4):
#         print(land[i][j])
#         land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
#         print(land[i-1][:j], ",", land[i-1][j+1:])
#         print(land[i][j])
#         print()
# print(max(land[-1]))