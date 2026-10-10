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
        best_attempt = h
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            hrs = compute_hours(mid)

            if hrs < best_attempt:
                best_attempt = hrs
            elif ans != -1:
                break

            if hrs < h:
                high = mid - 1
            else:
                low = mid + 1

            if hrs <= best_attempt:
                ans = mid

        return ans
