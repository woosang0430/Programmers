import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
input_list = list(map(int, input().split()))
M = int(input())
compare_list = list(map(int, input().split()))

# 정렬
input_list.sort()

# 비교 숫자 한 개씩 순회하며 이진탐색
for compare in compare_list:
  start, end = 0, N
  while start < end:
    mid = (start + end) // 2
    if input_list[mid] > compare:
      # 비교할 숫자가 더 작으면 end값 조정
      end = mid
    elif input_list[mid] < compare:
      # 비교할 숫자가 더 크면 start값 조정
      start = mid + 1
    else:
      # 값이 있으면 1
      print(1)
      break
  # break없이 종료되면 값이 없는 것
  else:
    print(0)

# input_list의 중복값을 제거하면 풀이가능
N = input()
N_list = set(input().split())
M = input()
M_list = list(input().split())

for m in M_list:
    print(1) if m in N_list else print(0)