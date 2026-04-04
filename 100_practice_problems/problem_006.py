# Write a program that will tell whether the number entered by the user is odd or even.

num = int(input("Enter the number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

ans = ["Even","Odd"]
print(ans[num%2])