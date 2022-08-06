# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def travesal(node):
            if not node:
                # l.append(None)
                return 
            
            travesal(node.left)
            l.append(node.val)
            travesal(node.right)
            
        travesal(root)
        return l