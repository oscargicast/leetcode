"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            aux = s[left]
            s[left] = s[right]
            s[right] = aux
            left += 1
            right -= 1
        

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    assert(s == ["o", "l", "l", "e", "h"])
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    assert(s == ["h", "a", "n", "n", "a", "H"])
