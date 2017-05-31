class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		dic = {'}' : '{', ']' : '[', ')' : '('}
		stack = []
		for item in s:
			if item in dic.values():
				stack.append(item)
			elif item in dic.keys():
				if stack == [] or dic[item] != stack.pop():
					return False
			else:
				return False
		return stack == []