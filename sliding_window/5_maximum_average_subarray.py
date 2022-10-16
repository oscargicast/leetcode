"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the
maximum average value and return this value.

Any answer with a calculation error less than 10^-5 will be accepted.
"""

from typing import List


def max_average(nums: List[int], k: int) -> float:
    current_sum = sum(nums[:k]) 
    max_average = current_average = current_sum / k 
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        current_average = current_sum / k 
        max_average = max(max_average, current_average)
    return max_average


if __name__ == "__main__":
    assert(max_average([1, 12, -5, -6, 50, 3], 4) == 12.75000)
    assert(max_average([5], 1) == 5.0)
