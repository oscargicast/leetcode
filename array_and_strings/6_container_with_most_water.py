"""
You are given an integer array height of length n.
There are n vertical lines, the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        lowest_height = 0
        left_to_right = None
        while left < right:
            # Computes width.
            width = right - left
            # Computes area.
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    assert(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
    assert(Solution().maxArea([1, 1]) == 1)
