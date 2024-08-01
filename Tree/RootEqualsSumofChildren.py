# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        sum = 0
        left_child = root.left
        right_child = root.right
        sum = left_child.val + right_child.val
        return root.val == sum
