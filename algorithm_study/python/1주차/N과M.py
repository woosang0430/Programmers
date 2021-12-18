import sys
sys.stdin = open('input.txt', 'rt')

# 백트래킹을 이용한 풀이
# DFS를 이용한 중복순열 문제에서 방문 조건(visited)을 넣어주어 중복되지 않는 수를 넣어준다.
# 재귀함수의 종류 조건으로 탐색 깊이가 leaf에 도달하면 답을 반환
# 재귀가 종료되면 마지막에 들어갔던 수의 방문 처리를 false로 바꿔준다.
def recursion(depth:int) -> None:
    if depth == leaf:
        print(*answer)
        return
    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            answer[depth] = i
            recursion(depth+1)
            visited[i] = False

if __name__ == "__main__":
    N, leaf = map(int, input().split())
    visited = [False] * (N+1)
    answer = [0] * leaf
    recursion(0)

"""
input
4 2

output
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
"""