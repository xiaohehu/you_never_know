# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced, _ = self.validate(root)
        return balanced
    def validate(self, root):
        if root == None:
            return True, 0
        balanced, leftHight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHight = self.validate(root.right)
        if not balanced:
            return False, 0
        
        return abs(leftHight - rightHight) < 2, max(leftHight, rightHight) + 1
        
