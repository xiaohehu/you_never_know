class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if s == None or t == None or len(s) != len(t):
			return False
		return self.getCharList(s) == self.getCharList(t)
	
	def getCharList(self, string):
		charList = [0] * 26
		for char in string:
			index = ord(char) - 97
			charList[index] += 1
		return charList
		