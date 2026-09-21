class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0
        profit = 0
        n = len(prices)

        while buy<sell<n:
            if prices[buy]>prices[sell] and sell <n-1:
                buy = sell
                sell+=1
            
            while sell<n-1 and prices[sell]<=prices[sell+1]:
                sell+=1
            
            profit = prices[sell] - prices[buy]
            if profit>maxProfit:
                maxProfit = profit
            sell+=1
            
        return maxProfit
            
            