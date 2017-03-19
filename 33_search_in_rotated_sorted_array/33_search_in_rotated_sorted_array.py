class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = 0
        if end == -1:
            return -1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid
                else:
                    start = mid
            else:
                if nums[end] >= target and nums[mid] <= target:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
