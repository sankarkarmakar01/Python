a = lambda a, b: a + b
print(a(1, 2))

res = lambda a, b, c: a if a > b else (b if b > c else c)
print(res(10, 2, 3))