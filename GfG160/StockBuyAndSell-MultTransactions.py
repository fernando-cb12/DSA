"""
    The cost of stock on each day is given in an array price[]. 
    Each day you may decide to either buy or sell the stock i
    at price[i], you can even buy and sell the stock on the same day.
    Find the maximum profit that you can get.

    Note: A stock can only be sold if it has been bought previously
    and multiple stocks cannot be held on any given day.
"""


from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        minPrice = prices[0]
        maxPrice = prices[0]
        profit = 0
        
        i = 0
        
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                maxPrice = prices[i+1]
                
            elif prices[i] > prices[i+1]:
                profit += maxPrice-minPrice
                minPrice = prices[i+1]
                maxPrice = prices[i+1]
                
            i+=1
                
                
        profit += maxPrice-minPrice  
                
        return profit
