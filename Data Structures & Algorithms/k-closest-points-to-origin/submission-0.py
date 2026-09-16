# I have unnaturally complicated this

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kClosestPoints = []
        for point in points:
            if not kClosestPoints:
                kClosestPoints.append(point)
                continue # I forgot to put this. 
            if (
                len(kClosestPoints) == k
                and self.calculate_distance(point) <= self.calculate_distance(kClosestPoints[-1])
            ) or len(kClosestPoints) != k:
                self.sort_helper(kClosestPoints, 0, len(kClosestPoints), point, k)

        return kClosestPoints

    def sort_helper(self, points, start, end, point, k):
        if len(points) == k and self.calculate_distance(point) <= self.calculate_distance(
            points[-1]
        ):
            return

        swap_index = start
        for i in range(start, end):
            if self.calculate_distance(points[i]) <= self.calculate_distance(point):
                if points[swap_index] != points[i]:
                    points[swap_index], points[i] = points[i], points[swap_index]
                swap_index += 1

        if swap_index == end:
            points.append(point)
        else:
            tmp = points[swap_index]
            points[swap_index] = point
            self.sort_helper(points, swap_index + 1, end, tmp,k) # This is slowly going into the territory 

    def calculate_distance(self, point):
        return pow((pow(point[0], 2) + pow(point[1], 2)), 0.5)
