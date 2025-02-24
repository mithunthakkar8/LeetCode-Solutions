# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Dictionary to store node references and their index
        node_store = {}  
        
        # Start traversal from the head of the linked list
        current = head  
        
        # Position counter to track the index of each node
        index = 0  
        
        # Traverse the linked list
        while current:
            # If the node is already in the dictionary, a cycle is detected
            if current in node_store:
                return True  # Cycle found

            # Store the current node reference and its position
            node_store[current] = index  
            
            # Move to the next node
            current = current.next  
            
            # Increment the position counter
            index += 1  

        # If traversal completes without revisiting a node, no cycle exists
        return False  
        
