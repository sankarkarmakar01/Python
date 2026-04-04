# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
from math import pi

r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

volume_cm3 = pi * (r ** 2) * h
volume_liters = volume_cm3 / 1000
cost_per_liter = 40
total_cost = volume_liters * cost_per_liter

print(f"Volume of the cylinder: {volume_cm3:.2f} cm³")
print(f"Total milk capacity: {volume_liters:.2f} liters")
print(f"Total cost of the milk: Rs. {total_cost:.2f}")
