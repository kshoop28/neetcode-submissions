# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        current = root

        while current:

            #if both values smaller -> left
            if p.val < current.val and q.val < current.val:
                current = current.left

            #if both values bigger -> right

            elif p.val > current.val and q.val > current.val:
                current = current.right
            
            else: 
                # so when they diverge or when p.val and q.val == current
                return current
              
              
