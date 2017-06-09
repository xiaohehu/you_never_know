class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stackList = []
		self.minList = []
		

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		if len(self.stackList) == 0 or x <= self.minList[-1]:
			self.minList.append(x)
		self.stackList.append(x)
		

	def pop(self):
		"""
		:rtype: void
		"""
		if self.stackList[-1] == self.minList[-1]:
			self.minList.pop()
		self.stackList.pop()
		

	def top(self):
		"""
		:rtype: int
		"""
		return self.stackList[-1]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.minList[-1]
		


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()