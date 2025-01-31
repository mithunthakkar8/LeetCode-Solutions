from typing import List  # Import List type for type hinting

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the given non-negative integer represented as a list of digits by one.

        Parameters:
        digits (List[int]): A list of integers representing a non-negative number (most significant digit first).

        Returns:
        List[int]: The updated list of digits after adding one.
        """
        # Start from the last digit (least significant digit)
        i = -1  

        # Traverse the list from the end towards the beginning
        while len(digits) >= abs(i):
            # If adding 1 to the current digit results in a carry
            if (digits[i] + 1) > 9:  
                # Set the current digit to 0 (carry over)
                digits[i] = 0  

                # If we reach the most significant digit and still have a carry
                if abs(i) >= len(digits):  
                    # Insert '1' at the beginning to handle cases like [9,9] -> [1,0,0]
                    digits.insert(0, 1)  
                    break  # Exit the loop since the addition is complete

            else:  
                # If no carry is needed, simply increment the current digit
                digits[i] += 1  
                break  # No further processing is needed

            # Move to the previous digit (towards the left)
            i -= 1  

        # Return the modified list representing the incremented number
        return digits  
