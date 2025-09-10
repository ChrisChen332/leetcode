class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def chours(self, piles: List[int], rates: int, h: int) -> int:
            hours = 0
            for i in piles:
                hour = i/rates
                if (int(hour) == hour):
                    hours += hour
                else:
                    hours += int(hour) + 1
            return hours
        low = 1
        high = max(piles)
        ans = -1
        while low <= high:
            mid = low + (high - low)//2
            if chours(self, piles,mid,h) > h:
                low = mid + 1
            elif chours(self, piles,mid,h) <= h:
                high = mid - 1
                ans = mid
        return ans