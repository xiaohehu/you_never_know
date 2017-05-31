# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		if not head:
			return None
		p = head
		while p:
			node = RandomListNode(p.label)
			node.next = p.next
			p.next = node
			p = node.next
		p = head
		while p:
			if p.random:
				p.next.random = p.random.next
				
			p = p.next.next
		
		pold = head
		newHead = head.next
		pnew = newHead
		while pnew.next:
			pold.next = pnew.next
			pold = pold.next
			pnew.next = pold.next
			pnew = pnew.next
		pold.next = None
		return newHead