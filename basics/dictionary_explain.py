student = {
    "name": "Sankar",
    "age": 21,
    "course": "Python"
}

print("Original Dictionary:", student)

# get() → Safe access
print("Name:", student.get("name"))
print("Marks (default):", student.get("marks", "Not Available"))

# keys() → All keys
print("Keys:", student.keys())

# values() → All values
print("Values:", student.values())

# items() → Key-value pairs
print("Items:", student.items())

# Add new key using assignment
student["marks"] = 85
print("After adding marks:", student)

# update() → Add / update multiple items
student.update({"age": 22, "city": "Delhi"})
print("After update:", student)

# setdefault() → Get value, add if missing
student.setdefault("grade", "A")
print("After setdefault:", student)

# pop() → Remove specific key
removed_value = student.pop("city")
print("Removed city:", removed_value)
print("After pop:", student)

# popitem() → Remove last inserted item
last_item = student.popitem()
print("Removed last item:", last_item)
print("After popitem:", student)

# copy() → Copy dictionary
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# len() → Number of items
print("Length:", len(student))

# sorted() → Sort keys
print("Sorted keys:", sorted(student))

# max() & min() → Based on keys
print("Max key:", max(student))
print("Min key:", min(student))

# clear() → Remove all items
student.clear()
print("After clear:", student)

# fromkeys() → Create new dictionary
subjects = ["Math", "Science", "English"]
# mark = [10,20,30]
marks = dict.fromkeys(subjects, 0)
print("Dictionary from fromkeys:", marks)
