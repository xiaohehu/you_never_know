class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        if end == -1:
            return 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        elif nums[start] > target:
            return 0
        elif nums[end] < target:
            return len(nums)
        else:
            return start + 1
