#!/usr/bin/python

class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		result = []
		hashMap = {}
		i = 0
		# Step 1 generate a dictionary, key is number, value is index
		while i < len(nums):
			hashMap[nums[i]] = i
			i += 1
		# Go through the list find dictionary has the number
		for item in nums:
			if hashMap.has_key(target - item):
				# In case same number reused 
				if nums.index(item) != hashMap[target - item]:
					result.append(nums.index(item))
					result.append(hashMap[target - item])
					break
		return result

haha = Solution()
print(haha.twoSum([3,2,4], 6))
		