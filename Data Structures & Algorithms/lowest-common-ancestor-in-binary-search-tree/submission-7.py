# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # can i find both the descendants from this node?
        # can i find both the descendands from the left node? 
        # etc

        # return the lowest node for which both can be found
        # values being unique means you just need to look for those values as opposed to that precise node
        def isInTree(node, p):
            if node is None:
                return False
            if node.val == p.val:
                return True
            else:
                return (isInTree(node.left, p) or isInTree(node.right, p))

        # its either in one branch or the other, not both 
        
        if isInTree(root, p) and isInTree(root, q):
            if isInTree(root.left, p) and isInTree(root.left, q):
                return self.lowestCommonAncestor(root.left, p, q)
            elif isInTree(root.right, p) and isInTree(root.right, q):
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
        else:
            return None
        
