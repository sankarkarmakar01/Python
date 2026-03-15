def extract_digits(num: int) -> None:
    if num < 0:
        num = abs(num)
    while num > 0:
        rem = num % 10
        print(rem)
        num //= 10


extract_digits(-123)
