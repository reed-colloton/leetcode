# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.root_i = 0
        idx = {x: i for i, x in enumerate(inorder)}
        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.root_i]
            self.root_i += 1
            mid = idx[root_val]
            left = dfs(l, mid - 1)
            right = dfs(mid + 1, r)
            return TreeNode(root_val, left, right)
        return dfs(0, len(preorder) - 1)