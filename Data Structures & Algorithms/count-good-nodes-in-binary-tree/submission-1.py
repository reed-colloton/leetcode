# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, root.val)


    def goodNodesHelper(self, root: TreeNode, highest_seen: float) -> int:
        if not root:
            return 0
        highest_seen = max(highest_seen, root.val)
        l_good = self.goodNodesHelper(root.left, highest_seen)
        r_good = self.goodNodesHelper(root.right, highest_seen)
        return int(highest_seen <= root.val) + l_good + r_good
    