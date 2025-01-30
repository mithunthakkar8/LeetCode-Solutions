import re
class Solution:
    def isValid(self, s: str) -> bool:
        # Define the regex pattern to match valid bracket pairs
        pattern = r'\(\)|\[\]|\{}'
        
        # Keep replacing valid pairs until no more can be found
        while re.search(pattern, s):
            s = re.sub(pattern, '', s)
        
        # If the string is empty, all brackets were matched correctly
        return len(s) == 0
