"""
Example 3: Given an integer array nums, find all the numbers x that satisfy the following:
x + 1 is not in nums, and x - 1 is not in nums.
"""


from typing import List


def find_all_numbers(nums: List[int]) -> List[int]:
    nums = set(nums)
    ans = []
    for num in nums:
        if num + 1 in nums and num - 1 in nums:
            ans.append(num)
    return ans


if __name__ == "__main__":
    assert(find_all_numbers([2, 1, 5, 3, 8, 9]) == [2])
    assert(find_all_numbers([2, 1, 5, 3, 8, 4]) == [2, 3, 4])
