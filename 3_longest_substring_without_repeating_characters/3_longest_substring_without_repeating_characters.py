#!/usr/bin/python
def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	result = []
	preResult = 0
	i = 0
	while i < len(s):
		if s[i] not in result:
			result.append(s[i])
			i += 1
		else:
			s = s[1:]
			if len(result) > preResult:
				preResult = len(result)
			result = []
			i = 0
	return max(preResult, len(result))


