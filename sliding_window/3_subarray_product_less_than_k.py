"""
Given an array of integers nums and an integer k,
return the number of contiguous subarrays where
# the product of all the elements in the subarray is strictly less than k.
# the sum of all the elements in the subarray is strictly less than k.
# the sum of all the elements in the subarray is strictly less than k.
a, b, c
a -b -c
"""

from typing import List


def number_of_contiguos_subarrays(nums: List[int], k: int) -> int:
    product = 1
    left = result = 0
    for right in range(0, len(nums)):
        product *= nums[right]
        while left <= right and product >= k:
            product //= nums[left]
            left += 1
        result += right - left + 1
    return result


if __name__ == "__main__":
    assert(number_of_contiguos_subarrays([10, 5, 2, 6], 100) == 8)

    # 10: [100]
    # 5: [100, 25] [25]: [25]
    # 2: [25 4] [4]
    # 6: [25 4 36]  


    assert(number_of_contiguos_subarrays([10, 5, 2, 6, 99], 100) == 9)
    assert(number_of_contiguos_subarrays([1, 2, 3], 0) == 0)
