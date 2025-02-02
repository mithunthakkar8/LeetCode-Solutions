class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list only once
        result = []
        
        # Define a helper function that performs the recursive in-order traversal
        def helper(node):
            if node:
                # Traverse the left subtree
                helper(node.left)
                # Append the current node's value
                result.append(node.val)
                # Traverse the right subtree
                helper(node.right)
        
        # Start the recursion with the root
        helper(root)
        return result
