"""
Example 1: Given an array of positive integers nums and an integer k,
find the length of the longest subarray whose sum is less than or equal to k.
"""

from typing import List


def longest_subarray(nums: List[int], k: int) -> int:
    left = 0
    max_len = 0
    sum_window = nums[0]
    for right in range(1, len(nums)):
        sum_window += nums[right]
        while left < right and sum_window > k:
            sum_window -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    assert(longest_subarray([3, 5, 1, 9, 7], 5) == 1)
    assert(longest_subarray([3, 1, 2, 7, 4, 2, 1, 1, 5], 8) == 4)
    assert(longest_subarray([3, 1, 3, 7, 5], 10) == 3)
    assert(longest_subarray([3, 1, 3, 2, 1, 1, 1], 10) == 6)
    assert(longest_subarray([3, 1, 2, 7, 4, 2, 1, 1, 5], 8) == 4)
