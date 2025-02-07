# Import the regular expression module
import re

# Define a class named Solution
class Solution:
    
    # Define a method to check if a string is a palindrome
    def isPalindrome(self, s: str) -> bool:
        
        # Initialize an empty string to store alphanumeric characters
        new_s = ''
        
        # Iterate over all alphanumeric substrings in lowercase form of input string
        for i in re.finditer('[0-9a-z]+', s.lower()):
            
            # Append the matched substring to new_s
            new_s += i.group()
        
        # Return True if new_s is equal to its reverse, otherwise return False
        return new_s[::-1] == new_s
