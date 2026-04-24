# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, float('-inf'))


    def goodNodesHelper(self, root: TreeNode, highest: float) -> int:
        if not root:
            return 0
        highest = max(highest, root.val)
        l_good = self.goodNodesHelper(root.left, highest) if root.left else 0
        r_good = self.goodNodesHelper(root.right, highest) if root.right else 0
        return int(highest <= root.val) + l_good + r_good
    