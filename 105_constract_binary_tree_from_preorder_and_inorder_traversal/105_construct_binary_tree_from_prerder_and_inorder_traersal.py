# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : rootIndex + 1], inorder[ : rootIndex])
        root.right = self.buildTree(preorder[rootIndex + 1 : ], inorder[rootIndex + 1: ])
        return root
        
