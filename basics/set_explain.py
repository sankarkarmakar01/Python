s = {1, 2, 3}
empty_set = set()   # NOT {}

print(s)
s.add(4)
print(s)

s.update([1,2,5])
print(s)

s.remove(2)
print(s)

s.discard(30)
print(s)

s.pop()
print(s)

s.clear()
print(s)

a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}

res = a.union(b) # or,  a | b
print(res)

res = a.intersection(b) # or,  a & b
print(res)

res = a.difference(b) # or,  a - b
print(res)

res = a.symmetric_difference(b) # or,  a ^ b
print(res)

# These methods modify the original set
# intersection_update()
# difference_update()
# symmetric_difference_update()

# Define sets
A = {1, 2, 3}
B = {3, 4, 5}
C = {1, 2}
D = {6, 7}

# isdisjoint() → No common elements
print(A.isdisjoint(D))   # True
print(A.isdisjoint(B))   # False

# issubset() → All elements of one set are in another
print(C.issubset(A))     # True
print(A.issubset(C))     # False

# issuperset() → Contains all elements of another set
print(A.issuperset(C))   # True
print(C.issuperset(A))   # False

# Create a set
numbers = {10, 5, 20, 15}

# len() → Total number of elements
print("Length:", len(numbers))

# max() → Largest element
print("Maximum:", max(numbers))

# min() → Smallest element
print("Minimum:", min(numbers))

# sum() → Sum of all elements
print("Sum:", sum(numbers))

# sorted() → Returns a sorted list (NOT a set)
sorted_numbers = sorted(numbers)
print("Sorted:", sorted_numbers)
