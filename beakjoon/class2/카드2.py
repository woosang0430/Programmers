from collections import deque

N = int(input())

num_list = deque([i for i in range(1, N+1)])

while len(num_list) != 1:
    num_list.popleft()
    num_list.append(num_list.popleft())

print(num_list[0])