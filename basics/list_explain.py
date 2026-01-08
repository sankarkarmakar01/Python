list1 = [1, 2, 3, 4, 5]
list2 = [10, 12]
print(list1)
list1.append(6)
print(list1)

list1.extend(list2)
print(list1)

list1.insert(0, 100)
print(list1)

list1.remove(12)
print(list1)

list1.pop()
print(list1)

list2.clear()
print(list2)

print(list1.index(6))
print(list1.index(100, 0))
print(list1.index(6,3,7))

list1.append(1)
print("Count: ", list1.count(1))

print("List: ", list1)
list1.sort()
print("Sort List: ", list1)
list1.sort(key = int, reverse = True)
print("Sort List reverse: ", list1)

list1.reverse()
print("Reverse List: ", list1)

print("List: ", list1)
list3 = list1.copy()
print("Copy List: ", list3)

print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))
print(sorted(list1))

new_list = [1, 2, 3]
print(new_list[1:3])
print(new_list * 3)
print(1 in new_list)
print(100 not in new_list)


for i in new_list:
    print(i)

