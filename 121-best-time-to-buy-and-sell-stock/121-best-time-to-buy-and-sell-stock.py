class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        Add to the max profit total if the current price is greater than previous, and we "sell" when the the opposite is true.

        
        There is one loop O(n) to compute the max profit before each each day and another loop O(n) to get the final max profit by compute the max profit after each day reversely and combine the "before day" max profit.
        
        iterate and look for min. 
        if cur item < min, update min / or save the difference in profit var.
        return profit
        """
        
        buy = prices[0]
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            else:
                if price - buy > profit:
                    profit = price - buy
                
        return profit
        