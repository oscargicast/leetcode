"""
704. Binary search

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.

If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right: 
        binary_index = (right + left) // 2
        if target == nums[binary_index]:
            return binary_index
        if target < nums[binary_index]:
            right = binary_index - 1
        else:
            left = binary_index + 1
    return -1


if __name__ == '__main__':
    assert(search([-1,0,3,5,9,12], 9) == 4)
    assert(search([-1,0,3,5,9,12], 2) == -1)
    assert(search([5], 5) == 0)
    assert(search([5], -5) == -1)
    assert(search([2, 5], 5) == 1)
