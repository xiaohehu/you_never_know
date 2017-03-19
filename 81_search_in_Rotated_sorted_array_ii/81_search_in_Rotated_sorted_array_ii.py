class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: bool
		"""
		start = 0;
		end = len(nums) - 1
		if end == -1:
			return False
		while start + 1 < end:
			mid = start + (end - start) / 2
			print(nums[start] , nums[mid] , nums[end])
			if nums[mid] == target or nums[start] == target or nums[end] == target:
				return True
			if nums[start] < nums[mid]:
				if target < nums[mid] and target > nums[start]:
					end = mid
				else:
					start = mid
			elif nums[start] > nums[mid]:
				if target < nums[end] and target > nums[mid]:
					start = mid
				else:
					end = mid
			else:
				if self.search(nums[start:mid], target):
					return True
				else:
					return self.search(nums[mid : end], target)
			
		if nums[start] == target or nums[end] == target:
				return True
		return False
