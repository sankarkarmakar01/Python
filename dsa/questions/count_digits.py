def count_digits(num: int) -> int:
    if num < 0:
        num = abs(num)
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


print(count_digits(123))
print(count_digits(-23))
