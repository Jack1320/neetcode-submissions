# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        index = {val: i for i, val in enumerate(inorder)}

        def build(p, lo, hi):
            if lo>hi:
                return None
            root_val = preorder[p]
            mid = index[root_val]
            left_size = mid-lo

            left = build(p+1, lo, mid-1)
            right = build(p+1+left_size,mid+1,hi)
            return TreeNode(root_val, left, right)

        return build(0,0,len(inorder)-1)
             