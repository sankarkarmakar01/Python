# Write a program that will give you the sum of 3 digits

num = int(input("enter the number: "))
add = 0

while num != 0:
    rem = num % 10
    add += rem
    num = int(num / 10)

print("Sum of digits is: ", add)
