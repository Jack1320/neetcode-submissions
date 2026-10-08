# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # just recursion again
        
        node = root
        
        if node is None:
            return 0

        max_depth = max(self.maxDepth(node.left), self.maxDepth(node.right))+1

        return max_depth