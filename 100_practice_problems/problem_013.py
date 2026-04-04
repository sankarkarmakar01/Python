# Write  a program that will tell whether the given number is divisible by 3 & 6.

num = int(input("enter the number: "))

if num % 3 == 0 and num % 6 == 0:
    print("true")
else:
    print("false")
