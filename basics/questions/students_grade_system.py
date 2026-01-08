# Write a program to take marks of a student and display:
#     Grade using if-elif-else
#     Pass or Fail using the ternary operator

marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B+")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C+")
elif marks >= 40:
    print("Grade: C")
elif marks < 40:
    print("Grade: D")
else:
    print("Enter a valid value.")

print("Pass" if marks >= 40 else "Fail")
