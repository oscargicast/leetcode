"""
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y]
and an integer limit, return a boolean array that represents the answer to each query.
A query is true if the sum of the subarray from x to y is less than limit, or false
otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]]
and limit = 13, the answer is [true, false, true]. For each query, the subarray sums
are [12, 14, 12].
"""

from typing import List, Union


def query(nums: List[int], queries: List[Union[int, int]], limit: int) -> List[bool]:
    prefix = [nums[0]] 
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    # prefix.append(0)
    print(f'nums: {nums}')
    print(f'prefix: {prefix}')
    answers = []
    query_sum_list = []
    for a, b in queries:
        query_sum = prefix[b] - prefix[a] + nums[a]
        # query_sum = prefix[b] - prefix[a - 1]
        query_sum_list.append(query_sum)
        answers.append(query_sum < limit)
    print(f'query sums: {query_sum_list}')
    print(f'answers: {answers}')
    return answers


if __name__ == "__main__":
    assert(
        query(
            [1, 6, 3, 2, 7, 2],
            [[0, 3], [2, 5], [2, 4]],
            13,
        ) == [True, False, True]
    )
