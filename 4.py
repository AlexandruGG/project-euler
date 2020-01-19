# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product


def is_palindrome(number: int):
    return str(number) == str(number)[::-1]


multiples = ([a, b] for a, b in product(range(100, 999), repeat=2) if is_palindrome(a * b))
maxPair = max(multiples, key=lambda pair: pair[0] * pair[1])
print(f"Largest palindrome: {maxPair[0] * maxPair[1]}")
