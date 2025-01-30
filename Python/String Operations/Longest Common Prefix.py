class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize an empty string to store the common prefix
        common_prefix = ''
        
        # Find the shortest string in the list to minimize comparison iterations
        shortest_word = min(strs, key=len)
        
        # Iterate through each character position in the shortest word
        for i in range(len(shortest_word)):
            # Create a set of characters at the current position from all words in the list
            letter_set = {word[i] for word in strs if word}
            
            # If all characters are the same, add to the common prefix
            if len(letter_set) == 1:
                common_prefix += list(letter_set)[0]
            else:
                # If characters differ, break the loop as the common prefix ends here
                break
             
        # Return the longest common prefix found
        return common_prefix
