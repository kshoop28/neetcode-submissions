# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque 
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        final_result = []


        while queue:
            level = []
            level_size = len(queue)

            for x in range(level_size):
                current = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            final_result.append(level[-1])
            #becauase level is the lsit actually
        
        return final_result





