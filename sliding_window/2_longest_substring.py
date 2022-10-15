"""
Example 2: You are given a binary substring s (a string containing only "0" and "1").
An operation involves flipping a "0" into a "1".
What is the length of the longest substring containing only "1"
after performing at most one operation?

For example, given s = "1101100111", the answer is 5.
If you perform the operation at index 2, the string becomes 1111100111.
"""


def longest_substring(s: str) -> int:
    # The window only can cantains a 0.
    left = zero_counter = max_len = 0
    for right in range(0, len(s)):
        if s[right] == "0":
            zero_counter += 1
        while left < right and zero_counter > 1:
            if s[left] == "0":
                zero_counter -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    assert(longest_substring("1101100111") == 5)
    assert(longest_substring("1111101111") == 10)
    assert(longest_substring("1111101011") == 7)
    assert(longest_substring("0111101011") == 6)
