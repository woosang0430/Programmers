'''
# input.txt
AbaAeCe
baeeACA

'''
# List version
import sys
from typing import List
sys.stdin = open('input.txt', 'rt')

def check_sentence(sentence:List) -> List:
  ret = [0] * 52
  for element in sentence:
    if element.isupper():
      ret[ord(element)-65] += 1
    else:
      ret[ord(element)-97] += 1
  return ret

first = check_sentence(input())
second = check_sentence(input())

for i in range(52):
  if first[i] != second[i]:
    print('NO')
    break
else:
  print('YES')

####

from collections import Counter

first = Counter(input())
second = Counter(input())

for key in first.keys():
  if not second.get(key) or first[key] != second[key]:
    print("NO")
    break
else:
  print("YES")

####

from typing import Dict, List

def Counter(sentence: List) -> Dict:
  ret = dict()
  for key in sentence:
    ret[key] = ret.get(key, 0) + 1
  return ret

first = Counter(input())
second = Counter(input())

for key in first.keys():
  if not second.get(key) or first[key] != second[key]:
    print("NO")
    break
else:
  print("YES")

