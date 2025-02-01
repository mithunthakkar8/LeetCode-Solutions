class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize the left and right bounds for the binary search range
        lower_bound, upper_bound = 0, x
        
        # Perform binary search to find the integer square root
        while lower_bound <= upper_bound:
            # Calculate the middle point (mid_point) of the current search range
            mid_point = lower_bound + (upper_bound - lower_bound) // 2
            mid_square = mid_point * mid_point  # Compute the square of the middle value

            # If we find the exact square root, return it
            if mid_square == x:
                return mid_point
            # If the square of mid_point is smaller than x, search in the right half
            elif mid_square < x:
                lower_bound = mid_point + 1
            # If the square of mid_point is greater than x, search in the left half
            else:
                upper_bound = mid_point - 1
        
        # Return the integer square root (upper_bound will be the largest value such that upper_bound*upper_bound <= x)
        return upper_bound
