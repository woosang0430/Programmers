N = int(input())
N_list = list(map(int, input().split()))
max_num = max(N_list)

visit_list = [True] * (max_num + 1)
result_list = []
for i in range(2, max_num+1):
    if visit_list[i]:
        if i in N_list:
            result_list.append(visit_list[i])
        compare_num = i
        while max_num >= compare_num:
            visit_list[compare_num] = False
            compare_num += i


print(len(result_list))