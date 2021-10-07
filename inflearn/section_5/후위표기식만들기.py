# input.txt
# 3+5*2/(7-2)

import sys
sys.stdin = open('input.txt', 'rt')

elements = input()
expression = ''
stack = []

for element in elements:
    if element.isdigit():
      expression += element
    else:
      if element == '(':
        stack.append(element)

      elif element in ['/', '*']:
        while stack and stack[-1] in ['/', '*']:
          expression += stack.pop()
        stack.append(element)

      elif element in ['+', '-']:
        while stack and stack[-1] != '(':
          expression += stack.pop()
        stack.append(element)
      
      elif element == ')':
        while stack and stack[-1] != '(':
          expression += stack.pop()
        stack.pop()

expression += ''.join(stack[::-1])
print(expression)