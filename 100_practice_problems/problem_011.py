# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

p = float(input("Enter the principle: "))
r = float(input("Enter the rate of interest: "))
t = int(input("Enter the time period(year): "))

SI = (p * r * t) / 100

print(f"Simple Interest: {SI}")
