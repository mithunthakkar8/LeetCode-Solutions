class Solution:
    # Function to calculate the maximum profit from stock prices
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price as the first price in the list
        min_price = prices[0]
        # Initialize the maximum profit as 0 (no profit at the start)
        max_profit = 0
        # Iterate over the prices starting from the second element
        for i in range(1, len(prices)):
            # Update the minimum price if a lower price is found
            if prices[i] < min_price:
                min_price = prices[i]
            # Update the maximum profit if the current profit exceeds previous max_profit
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        # Return the calculated maximum profit
        return max_profit
