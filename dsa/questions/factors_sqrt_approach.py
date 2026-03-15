from math import sqrt


def factors(num: int) -> list[int]:
    ans_list = []
    if num == 0:
        return []
    if num == 1:
        return [num]
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            ans_list.append(i)
            if num // i != i:
                ans_list.append(num // i)

    ans_list.sort()
    return ans_list


print(factors(1000))
