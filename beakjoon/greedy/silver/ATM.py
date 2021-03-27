n = int(input())
ret = 0
lst = []
for i in sorted(list(map(int, input().split()))):
    ret += i
    lst.append(ret)

print(sum(lst))