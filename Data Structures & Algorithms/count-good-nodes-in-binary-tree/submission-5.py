# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, highest: float) -> int:
            if not root:
                return 0
            highest = max(highest, node.val)
            l_good = dfs(node.left, highest) if node.left else 0
            r_good = dfs(node.right, highest) if node.right else 0
            return int(highest <= node.val) + l_good + r_good
    
        return dfs(root, float('-inf'))
    