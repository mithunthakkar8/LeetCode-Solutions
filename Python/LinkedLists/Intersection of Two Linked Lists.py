# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()  # Hash set to store visited nodes
        
        # Traverse list A and store nodes in the set
        currentA = headA
        while currentA:
            visited.add(currentA)
            currentA = currentA.next
        
        # Traverse list B and check if any node is already in the set
        currentB = headB
        while currentB:
            if currentB in visited:
                return currentB  # Intersection found
            currentB = currentB.next
        
        


            




