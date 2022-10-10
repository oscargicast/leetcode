"""
Example 2: Given a sorted array of unique integers and a target integer,
return true if there exists a pair of numbers that sum to target, false otherwise.

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""


def sum_target(sorted_int_list, target_sum):
    left_index = 0
    right_index = len(sorted_int_list) - 1
    while left_index < right_index:
        current_sum = sorted_int_list[left_index] + sorted_int_list[right_index]
        if current_sum == target_sum:
            return True
        if current_sum < target_sum:
            left_index += 1
        if current_sum > target_sum:
            right_index -= 1
    return False


if __name__ == "__main__":
    assert(sum_target([1, 2, 4, 6, 8, 9, 14, 15], 13) == True)
    assert(sum_target([1, 8, 14, 15], 11) == False)
    assert(sum_target([1, 8, 14, 15], 15) == True)
    assert(sum_target([1, 8, 14, 15], 22) == True)
