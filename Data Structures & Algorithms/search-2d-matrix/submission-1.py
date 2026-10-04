class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])
        low = 0
        high = len(matrix) * columns - 1

        while low <= high:
            mid = low + (high - low) // 2
            row, column = divmod(mid, columns)
            value = matrix[row][column]

            if target == value:
                return True
            if target > value:
                low = mid + 1
            else:
                high = mid - 1

        return False

        
        