class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        mid = 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            x = mid / len(matrix[0])
            y = mid % len(matrix[0])
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                start = mid
            if matrix[x][y] > target:
                end = mid
        if matrix[start / len(matrix[0])][start % len(matrix[0])] == target or matrix[end / len(matrix[0])][end % len(matrix[0])] == target:
            return True
        return False
