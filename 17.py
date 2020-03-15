# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


from typing import List

unique: List[str] = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                     'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens: List[str] = ['twenty', 'thirty', 'forty', 'fifty',
                   'sixty', 'seventy', 'eighty', 'ninety']


def len_below_100(n: int) -> int:
    return len(unique[n]) if n < 20 else len(tens[n // 10 - 2]) + len(unique[n % 10])


def len_below_1000(n: int) -> int:
    if (n < 100):
        return len_below_100(n)

    hundred_prefix = (n // 100) % 10
    hundred_suffix = n % 100
    length = 0

    if (hundred_prefix != 0):
        length += len(unique[hundred_prefix]) + len('hundred')

    if (hundred_suffix != 0):
        length += len('and') + len_below_100(hundred_suffix)

    return length


def calculate_all_lengths() -> int:
    return sum(len_below_1000(i) for i in range(1000))


print(f"Number of letters: {calculate_all_lengths() + len('onethousand')}")
