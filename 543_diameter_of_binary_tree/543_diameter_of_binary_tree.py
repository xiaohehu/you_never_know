tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        leftDepth = self.depthSubtree(root.left)
        rightDepth = self.depthSubtree(root.right)
        ans = leftDepth + rightDepth
        return max(max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)), ans)
        
    def depthSubtree(self, root):
        if root == None:
            return 0
        return max(self.depthSubtree(root.left), self.depthSubtree(root.right)) + 1
