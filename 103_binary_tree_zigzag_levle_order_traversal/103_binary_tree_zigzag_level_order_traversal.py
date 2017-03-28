tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        root_list = []
        if root == None:
            return ans
        root_list.append(root)
        flag = 0
        while len(root_list):
            new_root = []
            # Everytime need to add value to ans reverse the list
            if flag % 2:
                root_list.reverse()
            for node in root_list:
                new_root.append(node.val)
            ans.append(new_root)
            new_root = []
            # If list is reversed, need to reverse it again to add next level's nodes
            if flag % 2:
                root_list.reverse()
            for node in root_list:
                if node.left != None:
                    new_root.append(node.left)
                if node.right != None:
                    new_root.append(node.right)
            root_list = new_root
            flag += 1
        return ans
        
