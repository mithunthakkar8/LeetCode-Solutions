# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            # If the node is a leaf (no left or right child), return depth as 1
            if not root.left and not root.right:
                return 1
            
            # If the node has only a left child, recurse on the left subtree
            elif root.left and not root.right:
                return self.minDepth(root.left) + 1
            
            # If the node has only a right child, recurse on the right subtree
            elif not root.left and root.right:
                return self.minDepth(root.right) + 1
            
            # If the node has both left and right children, return the minimum depth of both subtrees + 1
            else:
                return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
        else:
            # If the root is None, return depth as 0
            return 0
