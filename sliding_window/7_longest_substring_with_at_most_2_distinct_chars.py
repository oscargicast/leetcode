"""
Given a string s, return the length of the longest substring that
contains at most two distinct characters.
"""


def longest_substring(s: str) -> int:
    max_len = left = 0
    char_count = {}
    for right in range(len(s)):
        char = s[right]
        if char_count.get(char):
            char_count[char] += 1
        else:
            char_count[char] = 1
        while len(char_count) > 2:
            char = s[left]
            if char_count.get(char):
                char_count[char] -= 1
                if char_count.get(char) == 0:
                    del char_count[char]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    assert(longest_substring("eceba") == 3)
    assert(longest_substring("ccaabbb") == 5)
    assert(longest_substring("abaccc") == 4)
    assert(longest_substring("xxxxx") == 5)
    assert(longest_substring("abcdefg") == 2)
