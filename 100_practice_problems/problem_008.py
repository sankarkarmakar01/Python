# Write a program to find the Euclidean distance between two coordinates.
import math

x1 = int(input("Enter the point of x1: "))
y1 = int(input("Enter the point of y1: "))

x2 = int(input("Enter the point of x2: "))
y2 = int(input("Enter the point of y2: "))

# ED = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
ED = math.dist([x1, y1], [x2, y2])

print("Euclidean distance between these coordinates is: ", ED)
