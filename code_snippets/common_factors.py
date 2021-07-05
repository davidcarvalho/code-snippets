def get_divisors(n):
    i = 1
    divisors = set()
    while i <= n:
        if n % i == 0:
            divisors.add(i)
        i += 1
    return divisors


def common_factors(a, b):
    return len(get_divisors(a).intersection(get_divisors(b)))


def count_common_factors(a, b):
    count = 0
    for i in range(1, min(a, b)):
        if a % i == 0 and b % i == 0:
            count += 1

    return count


print(count_common_factors(10, 15))
