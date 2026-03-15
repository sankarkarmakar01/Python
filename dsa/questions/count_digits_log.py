from math import log10


def count_digits_log(num: int) -> int:
    if num < 0:
        num = abs(num)
    if num == 0:
        return 0
    return int(log10(num) + 1)


print(count_digits_log(123))
print(count_digits_log(-2586))
print(count_digits_log(0))
