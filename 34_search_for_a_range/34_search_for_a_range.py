class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1, -1]
        start = 0
        end = len(nums) - 1
        if end == -1:
            return ans
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            ans[0] = start
        elif nums[end] == target:
            ans[0] = end
        
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            ans[1] = end
        elif nums[start] == target:
            ans[1] = start
        
        return ans
