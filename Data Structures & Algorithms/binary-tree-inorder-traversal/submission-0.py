# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        
        if not root:
            return ls
            
        ls.extend(self.inorderTraversal(root.left))
        ls.append(root.val)
        ls.extend(self.inorderTraversal(root.right))

        return ls
        


        
        