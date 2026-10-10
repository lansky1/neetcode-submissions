import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def compute_hours(num):
            attempts = 0
            for pile in piles:
                attempts += math.ceil(pile / num)
            return attempts

        low = 1
        high = max(piles)
        k = high

        while low <= high:
            mid = low + (high - low) // 2

            if compute_hours(mid) <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1

        return k
