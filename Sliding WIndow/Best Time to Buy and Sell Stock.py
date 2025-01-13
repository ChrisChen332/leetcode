from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = float('inf')
        for num in prices:
            if maxP < num - minP:
                maxP = num - minP
            if minP > num:
                minP = num
        return maxP