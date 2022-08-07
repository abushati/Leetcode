# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_val=0):
            if not node:
                return False
            
            current_val += node.val
            
            if not node.left and not node.right:
                return current_val == targetSum
            
            left_is_val = dfs(node.left,current_val)
            right_is_val = dfs(node.right, current_val)
            
            return left_is_val or right_is_val
        
        if not root:
            return False
        return dfs(root)