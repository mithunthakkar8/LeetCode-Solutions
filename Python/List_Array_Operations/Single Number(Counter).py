# Import the Counter class from the collections module to count occurrences of elements in the list
from collections import Counter 

# Define a class named Solution
class Solution:
    # Define a method that finds the single number in the list
    def singleNumber(self, nums: List[int]) -> int:
        # Iterate through the key-value pairs of the Counter dictionary (key = number, value = count)
        for k, v in Counter(nums).items():
            # Check if the count of the number is 1 (i.e., it appears only once)
            if v == 1:
                # Return the unique number
                return k
                # The break statement is unnecessary here since return already exits the function
                break  # (This line is redundant and can be removed)
