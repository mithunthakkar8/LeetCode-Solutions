# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_result = []
        q_result = []

        # Define a helper function that performs the recursive traversal
        def helper(node, result):
            if node is None:
                result.append(None)  # Track None to preserve structure
                return
            result.append(node.val)  # Append node value
            helper(node.left, result)  # Traverse left subtree
            helper(node.right, result)  # Traverse right subtree
        
        # Start the recursion with the root
        helper(p, p_result)
        helper(q, q_result)
        
        return p_result == q_result
