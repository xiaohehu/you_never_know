class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
	isNeg = False
	numList = []
	if x == 0:
		return 0
	if x < 0:
		x = 0 - x
		isNeg = True
	
	result = 0
	while 1:
		if x < 10:
			numList.append(x)
			break
		else:
			numList.append(x % 10)
			x = x // 10
	i = len(numList)
	for item in numList:
		result = result + item * (10 ** (i - 1))
		i -= 1
	if result > (2 ** 31 - 1):
	    return 0
	if isNeg:
		return  -result
	else:
	    return result
