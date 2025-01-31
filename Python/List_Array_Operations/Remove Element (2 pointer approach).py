class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer `j` to track the position for valid elements
        j = 0  

        # Iterate through the input list `nums`
        for i in range(len(nums)):  
            # If the current element is not equal to the target value
            if nums[i] != val:  
                # Move the current element to the position pointed by `j`
                nums[j] = nums[i]  
                # Increment `j` to the next position for the valid element
                j += 1  

        # Return the new length of the list (number of elements not equal to `val`)
        return j  
