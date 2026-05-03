# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path = float('-inf')
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            l, r = max(0, l), max(0, r)
            self.path = max(self.path, node.val + l + r)
            return  node.val + max(l, r)
        dfs(root)
        return int(self.path)