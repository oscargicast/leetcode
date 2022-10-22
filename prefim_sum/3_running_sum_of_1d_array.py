"""
1480. Running Sum of 1d Array

Given an array nums.
Wle define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from typing import List


def running_sum(nums: List[int]) -> List[int]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i-1])
    return prefix


if __name__ == "__main__":
    assert(running_sum([1,2,3,4]) == [1,3,6,10])
    assert(running_sum([1,1,1,1,1]) == [1,2,3,4,5])
    assert(running_sum([3,1,2,10,1]) == [3,4,6,16,17])
