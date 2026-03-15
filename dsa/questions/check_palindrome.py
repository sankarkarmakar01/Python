def check_palindrome(num: int) -> bool:
    if num < 0:
        return False

    temp = num
    rev = 0
    while num > 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num //= 10

    return rev == temp


ans = check_palindrome(153)
if ans:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
