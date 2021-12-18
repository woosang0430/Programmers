import sys
sys.stdin = open("input.txt", "rt")

count, target = map(int, input().split())
tree_list = list(map(int, input().split()))

# 초기 설정 -> 나무의 최대값 보다 많으면 안되므로 end를 최대값으로 설정
start, end = 1, max(tree_list)
while start <= end:
  mid = (start + end) // 2
  # 중간값을 기준으로 벌목하기!
  get_tree = sum([tree - mid for tree in tree_list if tree > mid])

  # 벌목한 나무가 많거나 같으면 나무를 더 조금 베기 위해 start값을 갱신
  if get_tree >= target:
    start = mid + 1
  # 적으면 나무를 더 많이 베어야 되므로 end값을 갱신
  else:
    end = mid - 1

print(end)
