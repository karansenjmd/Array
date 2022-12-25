class Solution:
    def maxProfit(self, prices) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit

prices = [7,1,5,3,6,4]
output = Solution().maxProfit(prices)
print(output)