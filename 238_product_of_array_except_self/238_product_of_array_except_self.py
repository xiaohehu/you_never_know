class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = []
		total = 1
		zeroCount = 0

		for i in range(len(nums)):
			if nums[i] == 0:
				zeroCount += 1
				continue
			total = total * nums[i]
		for i in range(len(nums)):
			if zeroCount == 0:
				result.append(total/nums[i])
			if zeroCount == 1:
				if nums[i] == 0:
					result.append(total)
				else:
					result.append(0)
			if zeroCount > 1:
				result.append(0)
					
		return result