# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        high = float('inf')
        low = float('-inf')
        def valid(low,high,node):
            if not node:
                return True
            if low < node.val < high:
                node_left = node.left
                node_right = node.right
                return valid(node.val, high, node_right) and valid(low, node.val, node_left)
            else:
                return False

        return valid(low,high,root)
        