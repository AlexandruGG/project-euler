# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


sumOfMultiples = sum(num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0)
print(f"Sum: {sumOfMultiples}")
