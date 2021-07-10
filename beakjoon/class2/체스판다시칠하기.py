Y, X = map(int, input().split())
board = [input() for _ in range(Y)]

result_list = []

# board를 넘어가지 않게 끝점 지정
for y in range(Y-7):
    for x in range(X-7):
        # chess_board의 왼쪽 위가 black인 경우와 white인 경우 저장
        black_case, white_case = 0, 0 
        # 8개씩 확인
        for row_idx in range(y, y+8):
            for col_idx in range(x, x+8):
                # board의 y, x좌표의 합으로 위치 잡기
                # 홀수인 경우
                if (row_idx + col_idx)%2:
                    # white로 시작하는 경우와 black으로 시작하는 경우 확인
                    if board[row_idx][col_idx] != 'W':
                        black_case += 1
                    if board[row_idx][col_idx] != 'B':
                        white_case += 1
                # 짝수면
                else:
                    if board[row_idx][col_idx] != 'B':
                        black_case += 1
                    if board[row_idx][col_idx] != 'W':
                        white_case += 1
        result_list.append(min(black_case, white_case))

print(min(result_list))