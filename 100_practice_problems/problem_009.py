# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

a = float(input("Enter the first angle length: "))
b = float(input("Enter the second angle length: "))
c = float(input("Enter the third angle length: "))

if a + b > c and a + c > b and b + c > a:
    print("The tringle is possible")
else:
    print("The tringle is not possible")
