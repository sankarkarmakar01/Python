print("Sankar")
a = "Hello"
print(a)

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# Indexing
name = "Sankar"
print(name[1])

# Slicing
print(name[0:3])
print(name[0:])
print(name[:6])
print(name[:])

# formatting
name = "Sankar"
age = 21

print("Hello, I am", name, ", and I am", age, "years old.")
print("Hello, I am {}, and I am {} years old.".format(name, age))
print(f"Hello, I am {name}, and I am {age} years old.")
