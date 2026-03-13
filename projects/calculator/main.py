from operations import *

print("\nWelcome to my calculator...\n")
def main():
    operation_list = ["+", "-", "*", "/", "%"]
    operation = input("Please enter a operation(I only perform +, -, *, / and %): ")
    if not len(operation) == 1 and not operation_list.count(operation) == 1:
        print("Please enter a valid operation...")
        return main()
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        ans = None
        match operation:
            case "+":
                ans = add(num1, num2)
                print("Answer:", ans)
                return None
            case "-":
                ans = sub(num1, num2)
                print("Answer:", ans)
                return None
            case "*":
                ans = mul(num1, num2)
                print("Answer:", ans)
                return None
            case "/":
                ans = div(num1, num2)
                print("Answer:", ans)
                return None
            case "%":
                ans = mod(num1, num2)
                print("Answer:", ans)
                return None
            case _:
                print("Please enter valid inputs...")
                return None

if __name__ == "__main__":
    main()