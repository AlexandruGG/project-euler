# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

from sympy import isprime


def get_nth_prime(n: int) -> int:
    i = prime_count = 0
    while prime_count < n:
        i += 1
        if isprime(i):
            prime_count += 1

    return i


print(f"10,001st prime: {get_nth_prime(10001)}")
