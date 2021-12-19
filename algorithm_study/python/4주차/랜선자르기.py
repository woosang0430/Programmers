import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

line_len, need_lines = map(int, input().split())
lines = [int(input()) for _ in range(line_len)]

start, end = 1, max(lines)

while start <= end:
    mid = (start+end)//2
    get_lines = sum([line//mid for line in lines])

    if get_lines >= need_lines:
        start = mid + 1
    else:
        end = mid - 1
print(end)