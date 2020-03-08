# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (13-numbers.txt)

from typing import List


def get_first_n_digits(n: int, x: int) -> int:
    return int(str(x)[:n])


with open('13-numbers.txt', 'r') as file:
    numbersList: List[int] = [int(line) for line in file]

numbers_sum = sum(numbersList)

print(f"First ten digits: {get_first_n_digits(10, numbers_sum)}")
