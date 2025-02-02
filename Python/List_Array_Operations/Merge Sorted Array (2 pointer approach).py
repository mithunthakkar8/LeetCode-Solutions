class Solution:
    # Method to merge two sorted arrays in-place
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # Pointer for nums2 (tracks elements being inserted)
        j = 0  
        
        # Pointer for nums1 (tracks the current position)
        i = 0  

        # Iterate through nums1 to insert elements from nums2 at correct positions
        while i < len(nums1):
            
            # Ensure there are still elements left in nums2
            if j < len(nums2):  
                
                # Check if nums2[j] should be inserted at the current position in nums1
                # Either nums2[j] is smaller than nums1[i], or we have passed all valid elements in nums1
                if nums1[i] > nums2[j] or i >= m + j:
                    
                    # Insert the current element of nums2 into nums1 at index i
                    nums1.insert(i, nums2[j])  
                    
                    # Remove the last element to maintain the original size of nums1
                    nums1.pop()  
                    
                    # Move to the next element in nums2
                    j += 1  
            
            # Move to the next position in nums1
            i += 1
