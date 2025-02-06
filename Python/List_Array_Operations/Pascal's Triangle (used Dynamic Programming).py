class Solution:
    # Function to generate Pascal's Triangle up to numRows
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize a 2D list with each row having 'i' zeros
        pascal = [[0] * i for i in range(1, numRows + 1)]
    
        # Iterate over each row
        for i in range(numRows):
            # Set the first element of each row to 1
            pascal[i][0] = 1
            # Set the last element of each row to 1
            pascal[i][-1] = 1
            # Fill in the inner values using the sum of two elements from the previous row
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

        # Return the generated Pascal's Triangle
        return pascal
