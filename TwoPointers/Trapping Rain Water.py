from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxL = height [i]
        maxR = height [j] 
        ans = 0
        while i <= j:
            if maxL >= maxR:
                if height[j] > maxR:
                    maxR = height[j]
                else:
                    ans += maxR - height[j]
                j -= 1
            else:
                if height[i] > maxL:
                    maxL = height[i]
                else:
                    ans += maxL - height[i]
                i += 1
        return ans