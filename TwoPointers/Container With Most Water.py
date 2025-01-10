from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxA = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            maxA = max(maxA, area)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            

        return maxA
        