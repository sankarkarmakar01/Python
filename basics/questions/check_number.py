# Write a program to check whether a number is positive, negative, or zero. If the number is positive, also check whether it is even or odd.

num = int(input("Enter a number: "))

if num == 0:
    print("Number is zero.")
elif num < 0:
    print("Number is negative.")
elif num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("And also it's a even number.")
    else:
        print("And also it's a odd number.")
else:
    print("Please enter a valid number.")