class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Initialize columnNumber to store the final result
        columnNumber = 0

        # Iterate through the reversed columnTitle to process from right to left
        for i, char in enumerate(reversed(columnTitle)):
            # Convert character to its corresponding numerical value (A=1, B=2, ..., Z=26)
            # Multiply by 26 raised to the power of its position to account for place value
            columnNumber += 26 ** i * (ord(char) - 64)

        # Return the computed column number
        return columnNumber
