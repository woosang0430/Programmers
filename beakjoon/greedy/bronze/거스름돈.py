changes = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
idx = 0

cnt = 0
while changes:
    if changes % coins[idx] == 0:
        cnt += (changes//coins[idx])
        break
    elif changes - coins[idx] < 0:
        idx += 1
        continue
    changes -= coins[idx]
    cnt += 1
print(cnt)
