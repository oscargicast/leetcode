"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


def sqrt(x: int) -> int:
    if x <= 1:
        return x
    left, right = 2, x // 2
    middle = (right + left) // 2
    while left <= right:
        middle = (right + left) // 2
        if middle ** 2 == x:
            return middle
        if middle ** 2 < x:
            left = middle + 1
        else:
            right = middle - 1
    if middle ** 2 > x:
        return middle - 1
    return middle


if __name__ == '__main__':
    assert(sqrt(4) == 2)
    assert(sqrt(8) == 2)
    assert(sqrt(6) == 2)
