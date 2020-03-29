# The Fibonacci sequence is defined by the recurrence relation: Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from typing import Generator


def fibonacci(a: int = 0, b: int = 1) -> Generator[int, None, None]:
    while True:
        yield b
        a, b = b, a + b


def get_fib_term_index(n: int) -> int:
    f = enumerate(fibonacci())
    while True:
        i, x = next(f)
        if (len(str(x)) >= n):
            break

    return i + 1


print(f"The {get_fib_term_index(1000)}-nth term has 1000 digits")
