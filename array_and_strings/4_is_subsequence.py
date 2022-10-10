"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            # If s is found, then increase the s index.
            if t[t_index] == s[s_index]:
                s_index += 1
            # If s is not found, then increase the t index.
            t_index += 1
        return s_index == len(s)


if __name__ == "__main__":
    assert(Solution().is_subsequence(s="abc", t="ahbgdc") == True)
    assert(Solution().is_subsequence(s="axc", t="ahbgdc") == False)
    assert(Solution().is_subsequence(s="aaaaaa", t="bbaaaa") == False)
