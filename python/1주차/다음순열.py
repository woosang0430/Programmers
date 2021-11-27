import sys
sys.stdin = open('input.txt', 'rt')

"""
참고 사이트
https://jeonggyun.tistory.com/110
- next_permutation 컨셉

뒤에서 부터 2개 씩 순회하며 2개의 값 중 뒤의 값이 더 큰 경우 다음 단계로 넘어간다.
    -> 앞의 값 l_idx, 뒤의값 r_idx

다음 단계 -> 다시 배열의 뒤에 부터 순회하며 l_idx의 값보다 큰값을 탐색하면 둘의 값을 swap한다
-> r_idx의 기준으로 왼쪽의 값은 그대로, 오른쪽의 값은 정렬한 후 answer에 붙여 반환한다.

배열의 길이가 1이거나 끝까지 순회해도 다음 값이 없는 경우 False를 반환시킨다.
"""
from typing import List

def next_permutations(num_list:List[int]) -> List[int] or bool:
    l_idx = N - 2
    while l_idx >= 0:
        r_idx = l_idx + 1
        if num_list[l_idx] < num_list[r_idx]:
            for x in range(N-1, 0, -1):
                if num_list[l_idx] < num_list[x]:
                    num_list[l_idx], num_list[x] = num_list[x], num_list[l_idx]
                    ret = num_list[:r_idx] + sorted(num_list[r_idx:])
                    return ret
        else:
            l_idx -= 1
    return False

if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int, input().split()))
    answer = next_permutations(num_list)
    if answer:
        print(*answer)
    else:
        print(-1)
"""
input
4
1 2 3 4

output
1 2 4 3
"""
