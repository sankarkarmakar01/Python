# ===============================
# Arithmetic Operators
# ===============================
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# ===============================
# Assignment Operators
# ===============================
print("\nAssignment Operators")
x = 5
x += 2
print("x += 2 ->", x)
x -= 1
print("x -= 1 ->", x)
x *= 3
print("x *= 3 ->", x)
x /= 2
print("x /= 2 ->", x)
x //= 2
print("x //= 2 ->", x)
x %= 2
print("x %= 2 ->", x)
x **= 3
print("x **= 3 ->", x)

# ===============================
# Comparison Operators
# ===============================
print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# ===============================
# Logical Operators
# ===============================
print("\nLogical Operators")
print("and:", a > 5 and b > 1)
print("or:", a > 20 or b > 1)
print("not:", not (a > 5))

# ===============================
# Bitwise Operators
# ===============================
print("\nBitwise Operators")
print("AND (&):", a & b)
print("OR (|):", a | b)
print("XOR (^):", a ^ b)
print("NOT (~a):", ~a)
print("Left Shift (a << 1):", a << 1)
print("Right Shift (a >> 1):", a >> 1)

# ===============================
# Membership Operators
# ===============================
print("\nMembership Operators")
nums = [1, 2, 3, 4, 5]
print("3 in nums:", 3 in nums)
print("10 not in nums:", 10 not in nums)

# ===============================
# Identity Operators
# ===============================
print("\nIdentity Operators")
m = [1, 2, 3]
n = m
o = [1, 2, 3]

print("m is n:", m is n)
print("m is o:", m is o)
print("m is not o:", m is not o)

# ===============================
# Operator Precedence
# ===============================
print("\nOperator Precedence")
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2
result3 = 10 + 5 ** 2
result4 = (10 + 5) ** 2

print("10 + 5 * 2 =", result1)
print("(10 + 5) * 2 =", result2)
print("10 + 5 ** 2 =", result3)
print("(10 + 5) ** 2 =", result4)
