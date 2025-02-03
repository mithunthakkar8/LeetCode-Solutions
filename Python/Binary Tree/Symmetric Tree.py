# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p_result = []
        q_result = []

        # Define a helper function that performs the recursive traversal
        def helper(node, result, compare = 0):
            if node is None:
                result.append(None)  # Track None to preserve structure
                return
            result.append(node.val)  # Append node value
            if compare == 0:
                helper(node.left, result)  # Traverse left subtree
                helper(node.right, result)  # Traverse right subtree
            elif compare == 1:
                helper(node.right, result,compare)  # Traverse right subtree
                helper(node.left, result,compare)  # Traverse left subtree
            
                
        
        # Start the recursion with the root
        helper(root, p_result)
        helper(root, q_result, compare =1)

        return p_result == q_result
