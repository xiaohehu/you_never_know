# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if head == None:
			return True
		if head.next == None:
			return True
		# Find tail of linked list
		tail = None
		listLength = 1
		tempHead = head
		while tempHead.next != None:
			tempHead = tempHead.next
			listLength += 1
		tail = tempHead
		# Find mid point of the linked list
		tempHead = head
		i = 0
		while i < listLength / 2:
			tempHead = tempHead.next
			i += 1
		mid = tempHead
		tempHead = None
		
		# Convert right half part of the linked list
		newMid = None
		while mid != None:
			temp = mid.next
			mid.next = newMid
			newMid = mid
			mid = temp
		# Compare first half hand second half of the Linked list
		i = 0
		while i < listLength / 2:
			if newMid.val != head.val:
				return False
			newMid = newMid.next
			head = head.next
			i += 1
		return True
			
		
		# Link tail to head, make it a cycle
		#tail.next = head
		# Go through the linked list from head and tail with different step length
		#for i in range(listLength / 2 + 1):
		#    if head.val != tail.val:
		#        return False
		#    head = head.next
		#    j = 0
		#    while j < listLength - 1:
		#        tail = tail.next
		#       j += 1
		#return True
		
		
			