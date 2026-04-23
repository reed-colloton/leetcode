# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = self.levelOrder(root)
        return [max(level) for level in levels]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = []
        queue = collections.deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()
            if len(levels) == depth:
                levels.append([])
            levels[depth].append(node.val)
            if node.left: queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))

        return levels   

