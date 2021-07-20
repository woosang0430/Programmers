N, step = map(int, input().split())

round_list = list(range(1, N+1))
move_len = step - 1
answer = []

for _ in range(N):
    move_len = move_len%len(round_list) if move_len >= len(round_list) else move_len
    answer.append(str(round_list.pop(move_len)))
    move_len += (step - 1)

print('<{0}>'.format(', '.join(answer)))