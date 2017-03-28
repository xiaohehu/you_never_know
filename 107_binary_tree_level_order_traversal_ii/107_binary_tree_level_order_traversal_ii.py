tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        root_list = []
        if root == None:
            return ans
        root_list.append(root)
        while len(root_list):
            temp_list = []
            for node in root_list:
                temp_list.append(node.val)
            ans.append(temp_list)
            temp_list = []
            for node in root_list:
                if node.left != None:
                    temp_list.append(node.left)
                if node.right != None:
                    temp_list.append(node.right)
            root_list = temp_list
        i = 0
        while i in range(len(ans)/2):
            temp = ans[i]
            ans[i] = ans[len(ans) - i - 1]
            ans[len(ans) - i - 1] = temp
            i += 1
        return ans
        
