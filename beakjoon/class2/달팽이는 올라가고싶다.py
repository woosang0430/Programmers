from math import ceil

A, B, V = map(int, input().split())

A -= B
V -= B

print(ceil(V/A))