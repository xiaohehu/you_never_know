# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root.left:
            nodeLeft = root.left
        else:
            nodeLeft = None
        if root.right:
            nodeRight = root.right
        else:
            nodeRight = None
        root.left = nodeRight
        root.right = nodeLeft
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        