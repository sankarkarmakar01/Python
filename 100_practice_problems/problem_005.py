# Write a program that will reverse a four-digit number.Also, it checks whether the reverse is true.

num = int(input("enter the number: "))
rev = 0

while num != 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num = int(num / 10)

print("Reverse: ", rev)
