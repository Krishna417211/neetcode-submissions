# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        diameter= 0

        def tree(node):

            nonlocal diameter

            if node is None:
                return 0


            left = tree(node.left)
            right = tree(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)


        tree(root)
        return diameter