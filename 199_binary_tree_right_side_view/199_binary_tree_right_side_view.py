# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        root_list = []
        if root == None:
            return ans
        root_list.append(root)
        while len(root_list):
            new_list = []
            for node in root_list:
                new_list.append(node.val)
            ans.append(new_list[-1])
            new_list = []
            for node in root_list:
                if node.left != None:
                    new_list.append(node.left)
                if node.right != None:
                    new_list.append(node.right)
            root_list = new_list
        return ans
