# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from sympy import isprime

start_sum = 2
sum_of_primes = sum(num for num in range(3, 2000000, 2) if isprime(num))

print(f"Sum of primes: {start_sum + sum_of_primes}")
