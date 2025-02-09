class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Create an empty list to store characters of the title
        Title_List = []
        
        # Loop until columnNumber reduces to 0
        while columnNumber > 0:
            # Adjust for 1-based indexing in Excel (makes it 0-based for base-26 conversion)
            columnNumber -= 1  
            
            # Find the corresponding letter and insert it at the beginning of the list
            Title_List.insert(0, chr(65 + (columnNumber % 26)))  
            
            # Move to the next "digit" in base-26 by dividing columnNumber by 26
            columnNumber //= 26  
        
        # Convert list of characters into a string and return the final column title
        return ''.join(Title_List)
