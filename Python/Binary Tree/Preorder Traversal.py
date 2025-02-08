# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
                
        # Initialize the result list only once
        result = []
        
        # Define a helper function that performs the recursive in-order traversal
        def helper(node):
            if node:
                # Append the current node's value
                result.append(node.val)
                # Traverse the left subtree
                helper(node.left)
                # Traverse the right subtree
                helper(node.right)
        
        # Start the recursion with the root
        helper(root)
        return result
