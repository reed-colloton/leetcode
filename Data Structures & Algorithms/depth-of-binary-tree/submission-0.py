# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root)

    def maxDepthHelper(self, root: Optional[TreeNode], depth = 0) -> int:
        if not root:
            return depth
        return max(self.maxDepthHelper(root.left, depth + 1), self.maxDepthHelper(root.right, depth + 1))