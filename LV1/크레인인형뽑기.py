def solution(board, moves):
  dolls_lst = [[0]]
  for i in range(len(board)):
    temp = []
    for j in range(len(board)):
      temp.append(board[j][i])
    dolls_lst.append(temp)
    # board에 2중 리스트 안의 값 index별 끼리 묶어 새로운(dolls_lst) 2중 리스트를 만든다.
  dolls_basket = []
  cnt = 0
  for i in moves: # moves를 dolls_lst의 인덱스로 접근
    for j in range(len(moves)):
      j %= len(dolls_lst[i])
      # moves의 길이를 j에 대입하면 dolls_lst의 인덱스 값을 벗어나므로 나머지로 접근
      if dolls_lst[i][j] != 0: # 0이 아니면 넣어라
        dolls_basket.append(dolls_lst[i][j])
        dolls_lst[i][j] = 0 # 인형을 뺏으니 0으로 재정의
        break
    if len(dolls_basket) > 1: # 길이가 2이상이여야 비교 가능
      if dolls_basket[-1] == dolls_basket[-2]: # 같으면 pop!pop!
        dolls_basket.pop()
        dolls_basket.pop()
        cnt+=2
    
  return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

"""  4 3 1 1 3 2 4
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1
"""