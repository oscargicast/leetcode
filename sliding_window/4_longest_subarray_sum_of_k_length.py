"""
Example 4: Given an integer array nums and an integer k,
find the sum of the subarray with the largest sum whose length is k.
"""

from typing import List


def max_sum_of_k_length(nums: List[int], k: int) -> int:
    left = max_sum = current_sum = 0
    for right in range(len(nums)):
        current_sum += nums[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[left]
            left += 1
    return max_sum


if __name__ == "__main__":
    assert(max_sum_of_k_length([6, 3, 7, 1, 9, 2], 1) == 9)
    assert(max_sum_of_k_length([6, 3, 7, 1, 9, 2], 2) == 11)
    assert(max_sum_of_k_length([6, 3, 7, 1, 9, 2], 3) == 17)
    assert(max_sum_of_k_length([6, 3, 7, 1, 9, 2], 4) == 20)
    assert(max_sum_of_k_length([1, 1, 1, 1, 1], 3) == 3)
    assert(max_sum_of_k_length([1, 1, 1, 1, 1], 5) == 5)
