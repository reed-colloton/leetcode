# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.goodNodesHelper(root, root.val)


    def goodNodesHelper(self, root: TreeNode, highest_seen: int) -> int:
        if not root:
            return 0
        highest_seen = max(highest_seen, root.val)
        if highest_seen <= root.val:
            return 1 + self.goodNodesHelper(root.left, highest_seen) + self.goodNodesHelper(root.right, highest_seen)
        else:
            return self.goodNodesHelper(root.left, highest_seen) + self.goodNodesHelper(root.right, highest_seen)
    