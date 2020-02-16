# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which: a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pyth_triplet(triplet_sum: int) -> int:
    for a in range(1, triplet_sum):
        for b in range(1, triplet_sum):
            c = triplet_sum - a - b
            if (a ** 2 + b ** 2) == c ** 2:
                print(f"Triplet found: ({a}, {b}, {c})")
                return a * b * c


print(f"Triplet product: {pyth_triplet(1000)}")
