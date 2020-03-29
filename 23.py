# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from sympy import divisors
from typing import List, Set
from itertools import product


def is_abundant(n: int) -> bool:
    return sum(divisors(n)) - n > n


def generate_sum_abundants_dict(abundants_list: List[int], max: int) -> Set[int]:
    is_sum_abundants_list: Set[int] = set()
    abundants_length = len(abundants_list)

    for i in range(0, abundants_length):
        for j in range(i, abundants_length):
            sum_abundants = abundants_list[i] + abundants_list[j]
            if (sum_abundants < max):
                is_sum_abundants_list.add(sum_abundants)

    return is_sum_abundants_list


def sum_non_abundants(max: int) -> int:
    abundants_list: List[int] = [i for i in range(1, max + 1) if is_abundant(i)]
    sum_abundants_dict = generate_sum_abundants_dict(abundants_list, max)

    return sum(i for i in range(0, max) if i not in sum_abundants_dict)


print(f"Non abundant sum: {sum_non_abundants(28123)}")
