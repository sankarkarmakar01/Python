from array import *

arr = array('i', [])

n = int(input("Enter the size of array: "))

for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)

print(arr)