# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # its either equal to the tree or a subroot of its branches

        def isEqual(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 is None and root2 is None:
                return True            
            elif root1 and root2 and root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right):
                return True
            else:
                return False
        if subRoot is None:
            return True
        if root is None:
            return False
        if root and subRoot and root.val == subRoot.val and isEqual(root, subRoot):
            return True
        elif self.isSubtree(root.left, subRoot):
            return True
        elif self.isSubtree(root.right, subRoot):
            return True
        else:
            return False