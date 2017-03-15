# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        node = result
        extra = 0
        while l1 or l2 or extra:
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
                
            node.next = ListNode((l1.val + l2.val + extra) % 10)
            extra = (l1.val + l2.val + extra) // 10
            node = node.next
            l1 = l1.next
            l2 = l2.next
        
        return result.next
                
            
