class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if len(digits) == 0:
			return []
		dic = { \
			"2" : ["a", "b", "c"], \
			"3" : ["d", "e", "f"], \
			"4" : ["g", "h", "i"], \
			"5" : ["j", "k", "l"], \
			"6" : ["m", "n", "o"], \
			"7" : ["p", "q", "r", "s"], \
			"8" : ["t", "u", "v"], \
			"9" : ["w", "x", "y", "z"], \
		}
		
		result = dic[digits[0]]
		n = len(digits)
		i = 1

		while i < n:
			result = self.combineChar(result, dic[digits[i]])
			i += 1
		return result
		
	def combineChar(self, c1, c2):
		combine = []
		for i in c1:
			for j in c2:
				combine.append(i + j)
		return combine