candles = [2,2,2]
turn = 1
while True:
    # 초의 갯수가 turn보다 작으면 더이상 못피우므로 break
    if len(candles) <= turn:
        break
    # 매 순간 높은 초 부터 사용하기 위해 정렬
    candles.sort(reverse=True)
    # 일수에 맞게 뺴주기
    for i in range(turn):
        candles[i] -= 1
    # 리스트의 0을 제거(리스트가 돌아가는 도중에는 리스트의 요소 제거 X)
    candles = [i for i in candles if i != 0]
    turn += 1

# 남아있는 초와 피워야될 초가 같으면 피워야할만큼 반환
if len(candles) == turn:
    ret = turn
# 피워야 할 초가 더 많으면 -1 을 하고 반환
elif len(candles) < turn:
    ret = turn - 1


print(ret)