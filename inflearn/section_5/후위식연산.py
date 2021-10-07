# input.txt
# 352+*9-

import sys
sys.stdin = open('input.txt', 'rt')

elements = input()
stack = []

for element in elements:
  if element.isdigit():
    stack.append(element)
  else:
    second = stack.pop()
    first = stack.pop()
    result = str(eval(first+element+second))
    stack.append(result)
answer = int(stack[0])
print(answer)