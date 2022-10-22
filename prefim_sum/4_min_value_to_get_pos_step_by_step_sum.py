"""
1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue
plus elements in nums (from left to right).

Return the minimum positive value of startValue
such that the step by step sum is never less than 1.
"""

from typing import List


def min_to_get_pos_sum(nums: List[int]) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i-1])
    min_prefix_value = min(prefix)
    if min_prefix_value > 0:
        return 1 
    return abs(min_prefix_value) + 1


if __name__ == "__main__":
    assert(min_to_get_pos_sum([-3,2,-3,4,2]) == 5)
    assert(min_to_get_pos_sum([1,2]) == 1)
    assert(min_to_get_pos_sum([1,-2,-3]) == 5)
    assert(min_to_get_pos_sum([2,3,5,-5,-1]) == 1)
    assert(min_to_get_pos_sum([-3,6,2,5,8,6]) == 4)
