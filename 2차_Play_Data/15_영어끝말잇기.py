def solution(n, words):
  players = [[] for _ in range(n)] # 각 플레이어 단어 모음
  answer = [words[0]] # 플레이중 나왔던 단어 저장
  players[0].append(words[0]) # 첫 단어 넣기

  for i in range(1, len(words)):
    turn = i%n # player 순서
    # 끝말잇기 룰 어기거나 답을 중복해서 말했으면 끝
    if words[i] in answer or answer[i-1][-1] != words[i][0]:
      return [turn+1, len(players[turn])+1] # 마지막 단어의 순서이기 때문에 +1
    
    else: # 아니면 이어가기
      players[turn].append(words[i])
      answer.append(words[i])
  # 반복문이 끝났는데 return이 안됐으면 올클린~
  return [0,0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))
# [3, 3]