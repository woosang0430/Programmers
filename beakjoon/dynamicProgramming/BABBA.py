k = int(input())

a, b = 1, 0
for _ in range(k):
    a, b = b, a+b
print(a, b)

###################
k = int(input())

num_list = [[1], [0]]
for i in range(k):
    num_list[0].append(num_list[1][i])
    num_list[1].append(num_list[1][i] + num_list[0][i])
print(num_list[0][-1], num_list[1][-1])