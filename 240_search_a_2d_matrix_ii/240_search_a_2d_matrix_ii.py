ass Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        column = len(matrix[0])
        if column == 0:
            return False

        for i in range(row):
            if target <= matrix[i][column - 1]:
                if self.checkAnswer(matrix[i], target):
                    return True
        return False
    
    def checkAnswer(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target or nums[end] == target:
            return True
        return False
        
