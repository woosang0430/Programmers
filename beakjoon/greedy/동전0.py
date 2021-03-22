n, k = map(int, input().split())
coins = []
for i in range(n):
    coin = int(input())
    if k >= coin:
        coins.append(coin)

answer = 0
for i in coins[::-1]:
    if k >= i:
        answer += (k//i)
        k %= i
    if k == 0:
        break
print(answer)