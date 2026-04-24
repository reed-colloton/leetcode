# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, highest: float) -> int:
            if not node:
                return 0
            highest = max(highest, node.val)
            l_good = dfs(node.left, highest)
            r_good = dfs(node.right, highest)
            return l_good + r_good + int(highest <= node.val)
    
        return dfs(root, float('-inf'))
    