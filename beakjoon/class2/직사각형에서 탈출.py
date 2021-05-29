x, y, w, h = map(int, input().split())

X = w - x
Y = h - y
x = min(X, x)
y = min(Y, y)
print(min(x, y))