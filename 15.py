# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Solution: binomial coefficient (x + y, y)

from sympy import binomial


def calculate_possible_routes(x: int, y: int) -> int:
    return binomial(x + y, y)


print(f"Possible routes: {calculate_possible_routes(20, 20)}")
