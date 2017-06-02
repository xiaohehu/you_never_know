class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		total = 0
		low = sys.maxint
		hight = 0
		for x in prices:
			if x - low > total:
				total = x - low
			if x < low:
				low = x
		return total