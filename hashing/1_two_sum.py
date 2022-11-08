"""
1. Two sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return [0, 0]


if __name__ == '__main__':
    assert(two_sum([2,7,11,15], 9) == [0,1])
    assert(two_sum([3,2,4], 6) == [1,2])
    assert(two_sum([3,3], 6) == [0,1])
