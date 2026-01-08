t = (1, 2, 3, 2, 2)
print(t.count(2))

t = (10, 20, 30, 20)
print(t.index(20))

t = (5, 2, 9, 1)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))   # returned a list

print(t[0])
print(t[1:3])  # (20, 30)


t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

print((1, 2) * 3)

print(2 in (1, 2, 3))


for item in (1, 2, 3):
    print(item)


# Packing
t = (10, 20, 30)
print(t)

# Unpacking
a, b, c = t
print(a, b, c)
