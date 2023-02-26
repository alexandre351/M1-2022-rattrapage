from functools import lru_cache
import pytest

@lru_cache(maxsize=10000)
def fibonacci(n: int):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    return 1 if (n == 1 or n == 2) else fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci_with_valid_input():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(13) == 233