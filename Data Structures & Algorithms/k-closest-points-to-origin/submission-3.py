# Some edge case
# Failing code
# This is the quickselect algorithm, used to identify kth smallest or largest element

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self._quick_sort(points, 0, len(points)-1, k)
        return points[:k]
    
    def _quick_sort(self, points, start, end, k):
        if start>=end:
            return

        swap_index = start
        for i in range(start, end):
            if self._calculate_distance(points[i]) <= self._calculate_distance(points[end]):
                points[swap_index], points[i] = points[i], points[swap_index]
                swap_index += 1

        points[swap_index], points[end] = points[end], points[swap_index]

        if k == swap_index+1:
            return
        elif k > swap_index+1:
            self._quick_sort(points, swap_index + 1, end, k-swap_index-1)
        else:
            self._quick_sort(points, start, swap_index - 1, k)

    def _calculate_distance(self, point):
        return pow((pow(point[0], 2) + pow(point[1], 2)), 0.5)
