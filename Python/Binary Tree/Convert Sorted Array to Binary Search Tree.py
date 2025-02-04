class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # If the list is empty, return None.
        if not nums:
            return None

        # Create a new TreeNode instance.
        bst = TreeNode()

        if len(nums) > 3:
            # Select the middle element as the root to ensure balance.
            root_loc = ceil((len(nums) - 1) / 2)
            bst.val = nums[root_loc]

            # Recursively build left and right subtrees.
            bst.left = self.sortedArrayToBST(nums[:root_loc])  # Left subtree from left half
            bst.right = self.sortedArrayToBST(nums[root_loc + 1:])  # Right subtree from right half

        elif len(nums) == 1:
            # If only one element, make it the root node.
            bst.val = nums[0]

        else:
            # If the list has 2 or 3 elements, manually construct the BST structure.
            try:
                bst.left = TreeNode(nums[0])  # First element as left child
                bst.val = nums[1]  # Second element as root
                
                # If there is a third element, assign it as the right child.
                bst.right = TreeNode(nums[2])
            except IndexError:
                pass  # Handles cases where the list has only two elements.

        return bst
