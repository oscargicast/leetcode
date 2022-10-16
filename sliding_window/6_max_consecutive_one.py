"""
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

from typing import List


def max_cons_ones(nums: List[int], k: int) -> int:
    # The longest windows only can have <= k zeros.
    max_len = 0
    left = 0
    curr = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    assert(max_cons_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6)
    assert(max_cons_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10)
