class Solution:
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:

        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            # Case 1: no left child
            if root.left is None:
                return root.right

            # Case 2: no right child
            if root.right is None:
                return root.left

            # Case 3: two children
            new_root = root.right
            current = new_root

            # Find the smallest node in the right subtree
            while current.left:
                current = current.left

            # Attach the old left subtree there
            current.left = root.left

            return new_root

        return root