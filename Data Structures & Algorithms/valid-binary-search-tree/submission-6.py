# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, a, b):
            if not node:
                return True
            if not a < node.val < b:
                return False
            l = dfs(node.left, a, min(b, node.val))
            r = dfs(node.right, max(a, node.val), b)
            return l and r 

        return dfs(root, float('-inf'), float('inf'))