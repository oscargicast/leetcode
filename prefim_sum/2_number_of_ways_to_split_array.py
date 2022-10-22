"""
Number of Ways to Split Array

Given an integer array nums, find the number of ways to split the array
into two parts so that the first section has a sum greater than or equal
to the sum of the second section.

The second section should have at least one number.
"""

from typing import List


def number_of_splits(nums: List[int]) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    ans = 0
    for i in range(len(nums) - 1):
        left_window = prefix[i]
        right_window = prefix[-1] - prefix[i]
        if right_window <= left_window:
            ans += 1
    return ans


if __name__ == '__main__':
    assert(number_of_splits([10, 4, -8, 7]) == 2)
    assert(number_of_splits([2, 3, 1, 0]) == 2)
