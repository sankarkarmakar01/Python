def check_armstrong(num: int) -> bool | None:
    if num == 0 or num == 1:
        return True

    def count_digits(n: int) -> int:
        if n < 0:
            n = abs(n)
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

    temp = num
    arm = 0
    while num > 0:
        rem = num % 10;
        arm = arm + pow(rem, count_digits(temp))
        num //= 10

    return temp == arm


ans = check_armstrong(371)
if ans:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
