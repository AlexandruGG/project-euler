# The following iterative sequence is defined for the set of positive integers:
#       n → n/2 (n is even)
#       n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Solution: iterate through numbers and generate collatz sequences, but cache their lengths in a dictionary and stop the generation if an entry is already present.

from typing import Dict, Tuple


def next_collatz(n): return n//2 if n % 2 == 0 else 3 * n + 1


def get_collatz_data(maximum: int) -> Tuple[int, int]:
    lengths_dict: Dict[int, int] = {1: 1}

    for number in range(1, maximum):
        current_length = 1
        n = number

        while n > 1:
            if n < number:
                current_length += lengths_dict[n] - 1
                break
            else:
                n = next_collatz(n)
                current_length += 1

        lengths_dict[number] = current_length

    max_number = max(lengths_dict, key=lengths_dict.get)
    max_length = lengths_dict[max_number]

    return max_number, max_length


number, length = get_collatz_data(1000000)
print(f"Max collatz start number: {number}")
print(f"Max collatz length: {length}")
