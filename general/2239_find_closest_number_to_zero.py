"""
2239. Find Closest Number to Zero

Given an integer array nums of size n,
return the number with the value closest to 0 in nums.

If there are multiple answers, return the number with the largest value.
"""

from typing import List


def closest_to_zero(nums):
    if not nums:
        return 0
    min_diff = abs(nums[0])
    ans = nums[0]
    for i in range(1, len(nums)):
        if abs(nums[i]) <= min_diff:
            if min_diff == abs(nums[i]):
                ans = max(ans, nums[i])
                continue
            ans = nums[i]
            min_diff = abs(ans)
    return ans


if __name__ == "__main__":
    assert(closest_to_zero([-9, 8, 55, 2, 7, 5]) == 2)
    assert(closest_to_zero([-4,-2,1,4,8]) == 1)
    assert(closest_to_zero([2,-1,1]) == 1)
    assert(closest_to_zero([2,1,-1]) == 1)
    assert(closest_to_zero([-1000, -1000]) == -1000)
