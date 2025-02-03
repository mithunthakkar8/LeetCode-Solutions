class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Helper function to perform depth-first search (DFS)
        def dfs(node, depth):
            # Base case: if the node is None, return the current depth
            if node is None: 
                return depth
            # Recursively compute the maximum depth by traversing left and right subtrees
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        # Start DFS traversal from the root node with an initial depth of 0
        return dfs(root, 0)
