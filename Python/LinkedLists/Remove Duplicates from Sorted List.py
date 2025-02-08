# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set to store unique values encountered in the list
        unique = set()       

        # Dummy node to handle edge cases like head being a duplicate
        dummy = ListNode(0)
        dummy.next = head

        def helper(prev, node):   
            if node:
                # If node value is unique, add it to the set and move forward
                if node.val not in unique:
                    unique.add(node.val)
                    helper(node, node.next)
                else:
                    # If duplicate, skip the node by adjusting prev.next
                    prev.next = node.next
                    helper(prev, node.next)
            return prev  # Return the last valid node

        # Start recursion from the dummy node
        prev = helper(dummy, head)

        # Return new head after removing duplicates
        return prev.next
