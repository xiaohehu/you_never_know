# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        rootList = []
        if root == None:
            return ans
        rootList.append(root)
        while len(rootList) :
            new_root = []
            for node in rootList:
                new_root.append(node.val)
            ans.append(new_root)
            new_root = []
            for node in rootList:
                if node.left != None:
                    new_root.append(node.left)
                if node.right != None:
                    new_root.append(node.right)
            rootList = new_root
        return ans
