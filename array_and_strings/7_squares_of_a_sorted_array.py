"""
Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""

from typing import List


def get_ordered_squares(nums: List[int]) -> List[int]:
    # Order using two pointers.
    left = 0
    right = len(nums) - 1
    ordered_abs_list = []
    while left <= right:
        if abs(nums[left]) <= abs(nums[right]):
            ordered_abs_list.append(nums[right] ** 2)
            right -= 1
            continue
        ordered_abs_list.append(nums[left] ** 2)
        left += 1
    # Order in n building a new array. 
    return ordered_abs_list[::-1]


if __name__ == '__main__':
    assert(get_ordered_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100])
    assert(get_ordered_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121])
