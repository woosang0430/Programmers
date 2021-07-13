lines, need_lines = map(int, input().split())
lines_len = [int(input()) for _ in range(lines)]

start, end = 1, max(lines_len)

while start <= end:
    mid = (start + end)//2
    get_lines = sum([line//mid for line in lines_len])
    if get_lines >= need_lines:
        start = mid + 1
    else:
        end = mid - 1

print(end)