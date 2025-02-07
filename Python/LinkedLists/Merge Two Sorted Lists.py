# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Merges two sorted linked lists into a single sorted list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # If only list1 exists, return it as the merged list
        if list1 and not list2:
            return list1

        # If only list2 exists, return it as the merged list
        if list2 and not list1:
            return list2
        
        # If both lists are empty, return None
        if not list1 and not list2:
            return None

        # Create a dummy head node to start the merged list
        head = ListNode()
        # Pointer to track the last node in the merged list
        current = head

        # Initialize head with the smaller value from list1 or list2
        if list1.val >= list2.val:
            head.val = list2.val
            list2 = list2.next
        else:
            head.val = list1.val
            list1 = list1.next

        # Traverse both lists until one becomes empty
        while list1 and list2:
            # If list2's value is smaller, add it to the merged list
            if list1.val >= list2.val:
                current.next = ListNode(list2.val)
                list2 = list2.next
            # If list1's value is smaller, add it to the merged list
            else:
                current.next = ListNode(list1.val)
                list1 = list1.next
            
            # Move current pointer to the newly added node
            current = current.next
            
        # Attach the remaining nodes from list1 if it's not empty
        if list1:
            current.next = list1
        # Attach the remaining nodes from list2 if it's not empty
        elif list2:
            current.next = list2

        # Return the merged linked list
        return head 
