# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		cur = None
		while head != None:
			temp = head.next
			head.next = cur
			cur = head
			head = temp
		return cur